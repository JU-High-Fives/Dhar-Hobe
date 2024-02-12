from django import forms
from .models import DeliveryRequest
from datetime import datetime, timedelta  # Import necessary modules with alphabetical order

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
            'preferred_delivery_time_start',
            'preferred_delivery_time_end',
            'special_instructions',
        ]

    def __init__(self, *args, **kwargs):
        """
        Initialize the form.
        Sets the minimum delivery time window to at least 2 hours from now.
        """
        super().__init__(*args, **kwargs)
        min_delivery_time = (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')
        self.fields['preferred_delivery_time_start'].widget.attrs['min'] = min_delivery_time

    def clean_preferred_delivery_time_end(self):
        """
        Clean method to validate preferred delivery end time.
        Ensures that delivery end time is after the start time.
        """
        start_time = self.cleaned_data['preferred_delivery_time_start']
        end_time = self.cleaned_data['preferred_delivery_time_end']
        if end_time <= start_time:
            raise forms.ValidationError('Delivery end time must be after start time')
        return end_time

    def clean_size_weight(self):
        """
        Clean method to validate size and weight input.
        Add your custom validation logic for size and weight here.
        """
        return self.cleaned_data['size_weight']

    # Additional custom validation methods as needed
