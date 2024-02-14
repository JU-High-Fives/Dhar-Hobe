from django.urls import path
from .views import add_item

urlpatterns = [
    path('add_item/', add_item, name='add_item'),
    # Other URLs...
]
