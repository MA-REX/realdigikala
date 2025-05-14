from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ShoppingAddress)
admin.site.register(OrderItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['date_ordered','last_update']
    inlines = [OrderItemInline]