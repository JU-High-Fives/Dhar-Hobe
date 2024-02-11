from django.shortcuts import render, redirect
from .models import DeliveryRequest

def delivery_request_create(request):
    if request.method == "POST":
        # Process form data and create DeliveryRequest object
        # Include validation for required fields
        new_request = DeliveryRequest.objects.create(
            user=request.user,
            # Extract data from form fields
            pickup_location=...,
            delivery_destination=...,
            # ... other fields
        )
        # Send notification to admin
        # ...
        return redirect("delivery_request_list")
    else:
        # Render form template
        return render(request, "delivery_request_form.html")


def delivery_request_list(request):
    requests = DeliveryRequest.objects.all()
    context = {"requests": requests}
    return render(request, "delivery_request_list.html", context)

def delivery_request_detail(request, pk):
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    context = {"request": request_obj}
    return render(request, "delivery_request_detail.html", context)

def delivery_request_update(request, pk):
    request_obj = get_object_or_404(DeliveryRequest, pk=pk)
    if request.method == "POST":
        # Update request object with new data
        # ...
        request_obj.save()
        return redirect("delivery_request_list")
    else:
        # Render update form with current data
        context = {"request": request_obj}
        return render(request, "delivery_request_update.html", context)
        request_obj.save()
        return redirect("delivery_request_list")
    