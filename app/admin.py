from django.contrib import admin
from .models import (
    Category,
    Profile,
    ShippingAdress,
    Brand,
    Product,
    CartItem,
    Cart,
    Order,
    OrderItem,
)

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "mobile_no1")


@admin.register(ShippingAdress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "address_1",
        "country",
        "state",
        "city",
        "zipcode",
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "brand",
        # "category",
        "qty",
        "img",
        "price",
    )


admin.site.register(Cart)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cart_id",
        "product_id",
        "qty",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "order_date",
        "amount",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "qty",
        "amount",
    )
