from django.db import models
from django.contrib.auth.models import User


class DeliveryRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    delivery_destination = models.CharField(max_length=255)
    size_weight = models.CharField(max_length=100)
    preferred_delivery_window = models.CharField(max_length=50, blank=True)
    special_instructions = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Assigned", "Assigned"), ("In transit", "In transit"), ("Delivered", "Delivered")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DeliveryProvider(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
