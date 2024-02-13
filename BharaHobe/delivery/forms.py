from django import forms
from .models import DeliveryRequest

class DeliveryRequestForm(forms.ModelForm):
    """
    Form for creating or updating a delivery request.
    """

    class Meta:
        model = DeliveryRequest
        # Specifies the model to use for this form and the fields to include.
        fields = [
            'pickup_location',  # Field for entering the pickup location.
            'delivery_destination',  # Field for entering the delivery destination.
            'size_weight',  # Field for specifying the size and weight of the delivery.
            'preferred_delivery_window',  # Field for selecting the preferred delivery window.
            'special_instructions',  # Field for providing any special instructions for the delivery.
        ]

    def __init__(self, *args, **kwargs):
        """
        Constructor for the DeliveryRequestForm.
        """
        super().__init__(*args, **kwargs)
        # Perform any additional initialization here if needed.
