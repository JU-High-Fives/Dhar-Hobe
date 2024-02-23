from django.shortcuts import render, redirect
from .forms import ItemForm, ItemSelectForm

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_added_successfully')  # Redirect to a success page
    else:
        form = ItemForm()
    return render(request, 'additem/add_item.html', {'form': form})

def select_item(request):
    if request.method == 'POST':
        form = ItemSelectForm(request.POST)
        if form.is_valid():
            selected_item = form.cleaned_data['item']
            # Do something with the selected item, e.g., pass it to a template
            return render(request, 'additem/selected_item.html', {'item': selected_item})
    else:
        form = ItemSelectForm()
    return render(request, 'additem/select_item.html', {'form': form})
