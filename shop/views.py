from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm ,UpdateUserInfo
from django.db.models import Q
from json import loads
from cart.cart import Cart
from payment.forms import ShoppingForm
from payment.models import ShoppingAddress, Order, OrderItem


# Create your views here.

def update_info(request):

    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shopping_user = ShoppingAddress.objects.get(user__id=request.user.id)

        form = UpdateUserInfo(request.POST or None, instance=current_user)
        sopping_form = ShoppingForm(request.POST or None, instance=shopping_user)
        if form.is_valid() or sopping_form.is_valid():
            form.save()
            sopping_form.save()
            messages.success(request, 'اطلاعات شما ویرایش شد')
            return redirect('index')
        return render(request, 'update_info.html', {'form': form, 'sopping_form': sopping_form})
    else:
        messages.error(request, 'ابتدا باید لاگین شوید')
        return redirect('login')


def index(request):
    all_products = Product.objects.all()

    return render(request, 'index.html', {'products': all_products})

def about(request):

    return render(request, 'about.html')

def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart

            if saved_cart:
                converted_cart =loads(saved_cart)
                cart = Cart(request)

                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('index')
        else:
            messages.error(request, 'مشکلی در ورود وجود داشت')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'رفتی با اینکه میدونستی ')
    return redirect('index')


def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, f' باریکلا {username}')
            return redirect('index')
        else:
            messages.success(request, 'مشکلی در ثبت نام شما وجود دارد')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form': form})

def product(request, pk):
    product_ = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product_})

def category(request, cat):
    cat = cat.replace('-',' ')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products,'category':category })
    except:
        messages.error(request, 'دسته بندی وجود ندارد')
        return redirect('index')


def category_summery(request):
    all_cat = Category.objects.all()

    return render(request, 'category_summery.html', {'category':all_cat})

def update_user(request):

    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'پروفایل شما ویرایش شد')
            return redirect('index')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.error(request, 'ابتدا باید لاگین شوید')
        return redirect('login')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == "POST":
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'رمز با موفقیت ویرایش شد')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = UpdatePasswordForm(request.POST)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.success(request, 'باید ابتدا لاگین بشی')
        redirect('login')
    return render(request, 'update_password.html', {})


def search(request):

    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, 'چنین محصولی وجود ندارد')
        else:
            return render(request, 'search.html', {'searched': searched})

    return render(request, 'search.html', {})


def user_orders(request):

    if request.user.is_authenticated:
        delivered_orders = Order.objects.filter(user = request.user, status='Delivered')
        other_orders = Order.objects.filter(user = request.user).exclude(status = 'Delivered')
        context= {
            'delivered': delivered_orders,
            'other': other_orders,
        }

        return render(request, 'orders.html', context)
    else:
        messages.success(request,'تو نمیتونی')
        return redirect('index')

def order_details(request, pk):

    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        items = OrderItem.objects.filter(order = pk)
        context = {'order': order, 'items': items}
        return render(request, 'order_details.html', context)
    else:
        messages.success(request,'تو نمیتونی')
        return redirect('index')




