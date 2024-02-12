from django.contrib import admin
from .models import PaymentModel, OrderModel

# Register your models here.

admin.site.register(PaymentModel)
admin.site.register(OrderModel)