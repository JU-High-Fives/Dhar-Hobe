from django.urls import path
from .views import make_payment

urlpatterns = [
    path('make-payment/', make_payment, name='make_payment'),
]
