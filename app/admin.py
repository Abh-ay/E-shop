from itertools import product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Cart, Product, OrderPlaced, Customer, User


# @admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'is_superuser', 'is_verified', 'email']


admin.site.register(User, UserAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_type',
                    'fabric_type', 'color_chart', 'company', 'available']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'user']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['status', 'customer', 'product', 'ordered_date', 'user']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'locality', 'city', 'zipcode']
