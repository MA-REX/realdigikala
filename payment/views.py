from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .forms import ShoppingForm
from .models import ShoppingAddress, Order ,OrderItem
from django.contrib import messages
from shop.models import Product, Profile
from django.contrib.auth.models import User
# Create your views here.

def payment_success(request):

    return render(request, 'payment/payment_success.html',{})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_totals()

    if request.user.is_authenticated:
        shopping_user = ShoppingAddress.objects.get(user__id = request.user.id)
        form = ShoppingForm(request.POST or None, instance=shopping_user)
        context = {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shopping_form': form}
        return render(request, 'payment/checkout.html', context)
    else:
        form = ShoppingForm(request.POST or None)
        context = {'cart_products': cart_products, 'shopping_form': form,}
        return render(request, 'payment/checkout.html', context)

def confirm_order(request):

    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_totals()

        user_shopping = request.POST
        request.session['user_shopping'] = user_shopping
        if request.user.is_authenticated:
            context = {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shopping_info': user_shopping}
            return render(request, 'payment/confirm_order.html', context)
        else:
            context = {'cart_products': cart_products, 'quantities': quantities, 'total': total,
                   'shopping_form': user_shopping, 'shopping_info': user_shopping}
            return render(request, 'payment/confirm_order.html', context)
    else:
        messages.success(request, 'دسترسی به این صفحه امکان پذیر نمی باشد')
        return redirect('index')


def process_order(request):

    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_totals()


        user_shopping = request.session.get('user_shopping')
        full_address = (f"{user_shopping['shopping_address1']}\n{user_shopping['shopping_address2']}"
                        f"\n{user_shopping['shopping_city']}\n{user_shopping['shopping_state']}\n"
                        f"{user_shopping['shopping_zipcode']}\n{user_shopping['shopping_country']}\n")
        full_name = user_shopping['shopping_full_name']
        email = user_shopping['shopping_email']

        if request.user.is_authenticated:
            user = request.user
            new_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shopping_address=full_address,
                amount_paid=total,
            )
            new_order.save()

            odr = get_object_or_404(Order, id=new_order.pk)
            for product in cart_products:
                prod =get_object_or_404(Product, id = product.id)
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for k,v in quantities.items():
                    if int(k) == product.id :
                        new_item = OrderItem(
                            order=odr,
                            product=prod,
                            price=price,
                            quantity=v,
                            user=user,
                        )
                        new_item.save()

            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]

            cu = Profile.objects.filter(user__id=request.user.id)
            cu.update(old_cart = "")
            messages.success(request, 'سفارش شما ثبت شد')
            return redirect('index')
        else:
            new_order = Order(
                full_name=full_name,
                email=email,
                shopping_address=full_address,
                amount_paid=total,
            )
            new_order.save()

            odr = get_object_or_404(Order, id=new_order.pk)
            for product in cart_products:
                prod = get_object_or_404(Product, id=product.id)
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for k, v in quantities.items():
                    if int(k) == product.id:
                        new_item = OrderItem(
                            order=odr,
                            product=prod,
                            price=price,
                            quantity=v,
                        )
                        new_item.save()

            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]

            messages.success(request, 'سفارش شما ثبت شد')
            return redirect('index')
    else:

        messages.success(request, 'دسترسی به این صفحه امکان پذیر نمی باشد')
        return redirect('index')
