from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeliveryRequestForm
from .models import DeliveryRequest
from django.contrib import messages
from django.utils.html import strip_tags

@login_required
def delivery_request_create(request):
    """
    Create a new delivery request.

    If the request method is POST, process the form submission and save the delivery request.
    If the form is valid, redirect to the delivery request list.
    If the form is invalid, render the form with errors.
    If the request method is GET, render the empty form.
    """
    if request.method == "POST":
        form = DeliveryRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()

            # Send confirmation message to user
            messages.success(request, 'Your delivery request has been submitted successfully.')

            # Notify admin
            admin_email = 'admin@example.com'  # Change this to your admin's email address
            subject = 'New Delivery Request'
            html_message = render_to_string('delivery/new_delivery_request.html', {'request': new_request})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'your@example.com', [admin_email], html_message=html_message)

            return redirect('delivery:delivery_request_list')
    else:
        form = DeliveryRequestForm()
    return render(request, "delivery/delivery_request_form.html", {'form': form})

def delivery_request_list(request):
    """
    List all delivery requests.
    """
    # Retrieve all delivery requests from the database
    requests = DeliveryRequest.objects.all()
    context = {"requests": requests}
    return render(request, "delivery/delivery_request_list.html", context)

def delivery_request_detail(request, pk):
    """
    View details of a specific delivery request.
    """
    # Retrieve the specific delivery request object or return a 404 error if not found
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    context = {"request": request_obj}
    return render(request, "delivery/delivery_request_detail.html", context)

@login_required
def delivery_request_update(request, pk):
    """
    Update a delivery request.
    """
    # Retrieve the specific delivery request object or return a 404 error if not found
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    if request.method == "POST":
        # Process form submission and update request object
        request_obj.save()
        return redirect("delivery_request_list")
    else:
        # Render update form with current data
        context = {"request": request_obj}
        return render(request, "delivery/delivery_request_update.html", context)

@login_required
def delivery_request_track(request, pk):
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    context = {"request": request_obj}
    return render(request, "delivery/delivery_request_track.html", context)

def delivery_complete(request, pk):
    """
    Complete a delivery request.
    """
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    if request.method == "POST":
        # Update the status of the delivery request to 'completed'
        request_obj.status = 'completed'
        request_obj.save()

        # Notify the user
        messages.success(request, 'Delivery completed successfully.')
        
        return redirect('delivery:delivery_request_list')
    return render(request, 'delivery/delivery_complete.html', {'request': request_obj})