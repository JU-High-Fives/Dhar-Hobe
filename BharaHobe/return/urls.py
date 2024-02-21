from django.urls import path
from . import views

urlpatterns = [
    path('initiate/<int:item_id>/', views.initiate_return_request, name='initiate_return_request'),
    path('confirmation/', views.return_request_confirmation, name='return_request_confirmation'),
]
