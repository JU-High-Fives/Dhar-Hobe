# urls.py
from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search_view, name='search'),
    path('results/', views.search_results_view, name='search_results'),
]
