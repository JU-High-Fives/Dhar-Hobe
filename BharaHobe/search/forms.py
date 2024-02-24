# forms.py
from django import forms
from .models import Product

class SearchForm(forms.Form):
    """
    Form for searching products.

    This form allows users to enter a search query to find products.

    Attributes:
        query (str): The search query entered by the user.
    """

    query = forms.CharField(label='Search', max_length=100)
