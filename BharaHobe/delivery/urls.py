from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    # Endpoint to create a new delivery request
    path('create/', views.delivery_request_create, name='delivery_request_create'),

    # Endpoint to list all delivery requests
    path('list/', views.delivery_request_list, name='delivery_request_list'),

    # Endpoint to view details of a specific request
    path('detail/<int:pk>/', views.delivery_request_detail, name='delivery_request_detail'),

    # Endpoint to update a delivery request (optional)
    path('update/<int:pk>/', views.delivery_request_update, name='delivery_request_update'),

    # Endpoint to track delivery progress (optional)
    path('track/<int:pk>/', views.delivery_request_track, name='delivery_request_track'),
    path('complete/<int:pk>/', views.delivery_complete, name='delivery_complete'),
]
