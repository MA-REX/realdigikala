from django.urls import path
from .views import payment_success, checkout, confirm_order, process_order
urlpatterns = [
    path('payment_success/',payment_success,name='payment_success'),
    path('checkout/',checkout, name='checkout'),
    path('confirm_order/',confirm_order, name='confirm_order'),
    path('process_order/', process_order, name='process_order'),

]