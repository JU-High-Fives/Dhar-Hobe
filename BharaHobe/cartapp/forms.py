from django import forms

class CartItemForm(forms.Form):
    """
    Form class for adding items to the cart.

    Attributes:
        product_id (IntegerField): The ID of the product to add to the cart.
        quantity (IntegerField): The quantity of the product to add to the cart.
    """

    product_id = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1)
