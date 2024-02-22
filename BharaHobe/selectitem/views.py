"""
 Import necessary functions and modules from Django
 Importing the Item model from models.py within the same app
 """

from django.shortcuts import render, redirect
from .models import Item  

"""
 Define a view function named select_item which renders a page to select items
"""
def select_item(request):
    
    """
     Retrieve all items from the database
    """
    items = Item.objects.all()

    """
     Render the select_item.html template with the items context
    """
    return render(request, 'selectitem/select_item.html', {'items': items})

   """
 Define a view function named process_selection which processes the selected item
"""
def process_selection(request):

    """
     Check if the request method is POST, which indicates form submission

    """
    if request.method == 'POST':

        """
         Retrieve the selected item's ID from the POST data
        """
        selected_item_id = request.POST.get('item_id')

        """
         Process the selected item (e.g., save it to the database, perform further actions)
         Redirect to a success page after processing
        """
        return redirect('success_page')

