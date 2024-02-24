# admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model.

    This class defines the appearance and functionality of the Product model
    in the Django admin interface.

    Attributes:
        list_display (tuple): Fields to display in the list view of the admin.
        search_fields (tuple): Fields to enable search functionality in the admin.
    """

    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')
