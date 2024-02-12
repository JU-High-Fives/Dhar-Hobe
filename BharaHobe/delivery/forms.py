from django import forms
from .models import DeliveryRequest

class DeliveryRequestForm(forms.ModelForm):
    """
    Form for creating or updating a delivery request.
    """

    class Meta:
        model = DeliveryRequest
        fields = [
            'pickup_location',
            'delivery_destination',
            'size_weight',
            'preferred_delivery_window',
            'special_instructions',
        ]
