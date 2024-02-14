from django.shortcuts import render, redirect
from .forms import ItemForm

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_added_successfully')  # Redirect to a success page
    else:
        form = ItemForm()
    return render(request, 'additem/add_item.html', {'form': form})
