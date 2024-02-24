# cartapp/urls.py

from django.urls import path
from .views import add_to_cart, get_cart_details

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', get_cart_details, name='get_cart_details'),
]
"""
URL patterns for cart-related functionality.

- /add-to-cart/: This endpoint allows users to add items to the cart.
- /cart/: This endpoint retrieves the details of the user's cart, including the items added to it.
"""
