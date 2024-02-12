from django.urls import path
from .views import advance_payment_view, payment_success, select_payment_method_view, monthly_payment_view, emi_payment_view, show_orders

urlpatterns = [
    path('show-orders/', show_orders, name='show_orders'),
    path('select_payment_method/', select_payment_method_view, name='select_payment_method'),
    path('advance_payment_form/', advance_payment_view, name='advance_payment_form'),
    path('monthly_payment_form/', monthly_payment_view, name='monthly_payment_form'),
    path('emi_payment_form/', emi_payment_view, name='emi_payment_form'),
    path('payment-success/', payment_success, name='payment_success'),
]
