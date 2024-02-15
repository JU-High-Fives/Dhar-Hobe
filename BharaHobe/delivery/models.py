from django.db import models
from django.contrib.auth.models import User

class DeliveryRequest(models.Model):
    """
    Model representing a delivery request.
    """

    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey linking to the User model, representing the user who made the delivery request.

    pickup_location = models.CharField(max_length=255, help_text="Location from where the package will be picked up")
    # CharField representing the pickup location of the package.

    delivery_destination = models.CharField(max_length=255, help_text="Destination where the package will be delivered")
    # CharField representing the delivery destination of the package.

    size_weight = models.CharField(max_length=100, help_text="Size and weight of the package")
    # CharField representing the size and weight of the package.

    preferred_delivery_window = models.CharField(max_length=50, blank=True, help_text="Preferred time window for delivery")
    # CharField representing the preferred delivery window for the package, can be blank.

    special_instructions = models.TextField(blank=True, help_text="Any special instructions for delivery")
    # TextField representing any special instructions for the delivery, can be blank.

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Assigned", "Assigned"),
        ("In transit", "In transit"),
        ("Delivered", "Delivered")
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, help_text="Status of the delivery request", default='pending')
    # CharField representing the status of the delivery request with predefined choices.
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the delivery request was created")
    # DateTimeField representing the date and time when the delivery request was created.
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the delivery request was last updated")
    # DateTimeField representing the date and time when the delivery request was last updated.

class DeliveryProvider(models.Model):
    """
    Model representing a delivery provider.
    """

    # Fields
    name = models.CharField(max_length=255, help_text="Name of the delivery provider")
    # CharField representing the name of the delivery provider.
    contact_details = models.CharField(max_length=255, help_text="Contact details of the delivery provider")
    # CharField representing the contact details of the delivery provider.
