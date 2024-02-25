from django import forms
from .models import Product

class rentform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['field1', 'field2', 'field3']  # Add fields from Product that you want to include in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Custom initialization or modifications to form fields can be done here
