from django.urls import path
from .views import search_view, search_results_view

urlpatterns = [
    path('search/', search_view, name='search'),  # URL to render the search form
    path('search-results/', search_results_view, name='search_results'),  # URL to handle search results
]

# cartapp/urls.py

from django.urls import path
from .views import add_to_cart, get_cart_details

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', get_cart_details, name='get_cart_details'),
]
