from django.contrib import admin
from . models import DeliveryRequest, DeliveryProvider

# Register your models here.
admin.site.register(DeliveryRequest)
admin.site.register(DeliveryProvider)
