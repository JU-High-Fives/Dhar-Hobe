from django.shortcuts import render, redirect
from .models import Item, ReturnRequest
from . forms import ReturnRequestForm

def initiate_return_request(request, item_id):
    """
    View function to initiate a return request for a specific item.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item for which the return request is initiated.

    Returns:
        HttpResponse: Renders a form for initiating return request or redirects to confirmation page.

    """
    # Retrieve the item based on item_id from the database
    item = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = ReturnRequestForm(request.POST)
        if form.is_valid():
            # If form data is valid, save the return request
            return_request = form.save(commit=False)
            return_request.user = request.user
            return_request.item = item
            return_request.save()
            # Redirect to the return request confirmation page
            return redirect('return_request_confirmation')
    else:
        # If the request method is GET, initialize an empty form
        form = ReturnRequestForm()
    
    # Render the template with the form and item object
    return render(request, 'return/initiate_return_request.html', {'form': form, 'item': item})

def return_request_confirmation(request):
    """
    View function to render the confirmation page for a return request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the return request confirmation page.

    """
    # Render the return request confirmation template
    return render(request, 'return/return_request_confirmation.html')
