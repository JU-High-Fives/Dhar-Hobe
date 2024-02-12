from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DeliveryRequestForm
from .models import DeliveryRequest

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
            # Send notification to admin
            # ...
            return redirect("delivery_request_list")
    else:
        form = DeliveryRequestForm()
    return render(request, "delivery_request_form.html", {'form': form})


def delivery_request_list(request):
    """
    List all delivery requests.
    """
    requests = DeliveryRequest.objects.all()
    context = {"requests": requests}
    return render(request, "delivery_request_list.html", context)


def delivery_request_detail(request, pk):
    """
    View details of a specific delivery request.
    """
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    context = {"request": request_obj}
    return render(request, "delivery_request_detail.html", context)


@login_required
def delivery_request_update(request, pk):
    """
    Update a delivery request.
    """
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    if request.method == "POST":
        # Process form submission and update request object
        # ...
        request_obj.save()
        return redirect("delivery_request_list")
    else:
        # Render update form with current data
        context = {"request": request_obj}
        return render(request, "delivery_request_update.html", context)
