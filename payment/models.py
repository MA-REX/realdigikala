from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from shop.models import Product
from django_jalali.db import models as jmodels
import jdatetime

# Create your models here.

class ShoppingAddress(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    shopping_full_name = models.CharField(max_length=100)
    shopping_email = models.CharField(max_length=100)
    shopping_address1 = models.CharField(max_length=250, blank=True)
    shopping_address2 = models.CharField(max_length=250, blank=True,null=True)
    shopping_city = models.CharField(max_length=25, blank=True)
    shopping_state = models.CharField(max_length=25, blank=True)
    shopping_zipcode = models.CharField(max_length=25, blank=True)
    shopping_country = models.CharField(max_length=25, default='IRAN')

    # class Meta:
    #     verbose_name_plural = 'Shopping Addresses'

    def __str__(self):
        return self.shopping_full_name

def create_shopping_user(sender, instance, created, **kwargs):
    if created:
        user_shopping= ShoppingAddress(user=instance)
        user_shopping.save()

post_save.connect(create_shopping_user, sender=User)



class Order(models.Model):
    STATUS_ORDER=[
        ('Pending','در انتظار پرداخت'),('Processing', 'در حال پردازش'),('shipped', 'ارسال شده به پست'),
        ('Delivered', 'تحویل داده شده'),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    shopping_address = models.TextField(max_length=1000)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=12)
    date_ordered = jmodels.jDateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_ORDER, default='Pending')
    last_update = jmodels.jDateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_status = Order.objects.get(id=self.pk).status

            if old_status != self.status:
                self.last_update = jdatetime.datetime.now()

        super().save(*args, **kwargs)
    def __str__(self):
        return self.full_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return self.product.name




