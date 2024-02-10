from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    # Create new delivery request
    path('create/', views.delivery_request_create, name='delivery_request_create'),

    # List all delivery requests
    path('list/', views.delivery_request_list, name='delivery_request_list'),

    # View details of a specific request
    path('detail/<int:pk>/', views.delivery_request_detail, name='delivery_request_detail'),

    # Update a delivery request (optional)
    path('update/<int:pk>/', views.delivery_request_update, name='delivery_request_update'),

    # Track delivery progress (optional)
    # path('track/<int:pk>/', views.DeliveryRequestTrackView.as_view(), name='delivery_request_track'),
]
