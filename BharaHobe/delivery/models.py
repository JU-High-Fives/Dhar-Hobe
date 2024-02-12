from django.db import models
from django.contrib.auth.models import User

class DeliveryRequest(models.Model):
    """
    Model representing a delivery request.
    """

    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255, help_text="Location from where the package will be picked up")
    delivery_destination = models.CharField(max_length=255, help_text="Destination where the package will be delivered")
    size_weight = models.CharField(max_length=100, help_text="Size and weight of the package")
    preferred_delivery_window = models.CharField(max_length=50, blank=True, help_text="Preferred time window for delivery")
    special_instructions = models.TextField(blank=True, help_text="Any special instructions for delivery")
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Assigned", "Assigned"),
        ("In transit", "In transit"),
        ("Delivered", "Delivered")
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, help_text="Status of the delivery request")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the delivery request was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the delivery request was last updated")

class DeliveryProvider(models.Model):
    """
    Model representing a delivery provider.
    """

    # Fields
    name = models.CharField(max_length=255, help_text="Name of the delivery provider")
    contact_details = models.CharField(max_length=255, help_text="Contact details of the delivery provider")
