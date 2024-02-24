from django.shortcuts import render, redirect
from .forms import ItemForm, ItemSelectForm 

""" 
 Import necessary functions and modules from Django
 Importing forms from forms.py within the same app

 View function for adding an item
"""
def add_item(request):

    """
    Renders a form to add an item and processes the form submission.

    If the request method is POST and the form data is valid, saves the form data
    and redirects to a success page.
    If the request method is GET, renders an empty form to add an item.
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_added_successfully')  

            """
             Redirect to a success page
            """
    else:
        form = ItemForm()
    return render(request, 'additem/add_item.html', {'form': form})
"""
 View function for selecting an item
"""
def select_item(request):

    """
    Renders a form to select an item and processes the form submission.

    If the request method is POST and the form data is valid, retrieves the selected item
    and renders a page with information about the selected item.
    If the request method is GET, renders a form to select an item.
    """
    if request.method == 'POST':
        form = ItemSelectForm(request.POST)
        if form.is_valid():
            selected_item = form.cleaned_data['item']
            
            """
             Do something with the selected item, e.g., pass it to a template
            """
            return render(request, 'additem/selected_item.html', {'item': selected_item})
    else:
        form = ItemSelectForm()
    return render(request, 'additem/select_item.html', {'form': form})
