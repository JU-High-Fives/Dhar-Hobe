from django.urls import path
from .views import search_view, search_results_view

urlpatterns = [
    path('search/', search_view, name='search'),  # URL to render the search form
    path('search-results/', search_results_view, name='search_results'),  # URL to handle search results
]
