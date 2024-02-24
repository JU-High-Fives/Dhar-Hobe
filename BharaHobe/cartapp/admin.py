from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Cart model.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
    """

    list_display = ('user', 'created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CartItem model.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
    """

    list_display = ('cart', 'product', 'quantity')
