from django import forms
from .models import Item 

"""
 Import necessary modules
 Importing the Item model from models.py within the same app
 Form for adding an item
"""
class ItemForm(forms.ModelForm):

    """
    Form class for adding an item.
    Inherits from Django's ModelForm class to create a form based on the Item model.
    Specifies the fields to include in the form.
    """
    class Meta:
        model = Item  

        """
         Specify the model to use for the form
        """
        fields = ['name', 'description'] 

        """
         Specify the fields to include in the form

        """
# Form for selecting an item
class ItemSelectForm(forms.Form):

    """
    Form class for selecting an item.
    
    Creates a form with a single field representing a choice of items.
    The queryset for the choice field is set to all items in the Item model.
    """
    item = forms.ModelChoiceField(queryset=Item.objects.all())  

    """
     Define a choice field for selecting an item

    """