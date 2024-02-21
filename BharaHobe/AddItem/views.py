"""
 Import necessary functions and modules from Django
 Importing the ItemForm from forms.py within the same app

"""
from django.shortcuts import render, redirect
from .forms import ItemForm 

"""
 Define a view function named add_item which handles adding an item
"""
def add_item(request):
    """
    Check if the request method is POST, which indicates form submission

    """
    if request.method == 'POST':
        """
         If it's a POST request, initialize a form instance with the data from the request
        """
        form = ItemForm(request.POST)
        """
         Check if the submitted form data is valid
        """
        if form.is_valid():
            """
             If the form data is valid, save the form (which also creates a new item)
            """
            form.save()
            """
             Redirect to a success page after adding the item successfully
            """
            return redirect('item_added_successfully')
    else:
        
        form = ItemForm()

        """
         If it's not a POST request, instantiate an empty form
         Render the add_item.html template with the form context
         
        """
    return render(request, 'additem/add_item.html', {'form': form})
