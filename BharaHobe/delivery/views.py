from django.shortcuts import render, redirect
from .models import DeliveryRequest

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import DeliveryRequest

@login_required
def delivery_request_create(request):
    if request.method == "POST":
        form = DeliveryRequestForm(request.POST)  # Assuming you have a DeliveryRequestForm
        if form.is_valid():
            new_request = form.save(commit=False)  # Create DeliveryRequest instance without saving
            new_request.user = request.user  # Assign current user to the request
            new_request.save()  # Save the DeliveryRequest object
            # Send notification to admin (specific implementation based on your preferences)
            # ...
            return redirect("delivery_request_list")
        else:
            # Display form with errors
            return render(request, "delivery_request_form.html", {'form': form})
    else:
        form = DeliveryRequestForm()  # Create an empty form instance
        return render(request, "delivery_request_form.html", {'form': form})


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
    