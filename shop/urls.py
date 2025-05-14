from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('signup/', signup_user, name='signup'),
    path('product/<int:pk>/',product, name='product'),
    path('category/<str:cat>/',category, name='category'),
    path('category/', category_summery, name= 'category_summery'),
    path('update_user/', update_user , name='update_user'),
    path('update_password/', update_password, name='update_password'),
    path('update_info/', update_info, name='update_info'),
    path('search/', search, name='search'),
    path('orders/', user_orders, name='orders'),
    path('order_details/<int:pk>', order_details, name='order_details'),
]