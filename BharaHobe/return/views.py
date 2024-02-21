from django.shortcuts import render, redirect
from .models import Item, ReturnRequest
from .forms import ReturnRequestForm

def initiate_return_request(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ReturnRequestForm(request.POST)
        if form.is_valid():
            return_request = form.save(commit=False)
            return_request.user = request.user
            return_request.item = item
            return_request.save()
            return redirect('return_request_confirmation')
    else:
        form = ReturnRequestForm()
    return render(request, 'return/initiate_return_request.html', {'form': form, 'item': item})

def return_request_confirmation(request):
    return render(request, 'return/return_request_confirmation.html')