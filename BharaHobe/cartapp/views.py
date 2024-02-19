# views.py
from django.shortcuts import render
from .models import Product

def search_view(request):
    return render(request, 'search_form.html')

def search_results_view(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})


def search(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        # Perform search query
        results = Product.objects.filter(name__icontains=query)
    
    return render(request, 'search_results.html', {'results': results, 'query': query})

from django.shortcuts import render
from .forms import SearchForm
from .models import Product

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'form': form, 'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})
