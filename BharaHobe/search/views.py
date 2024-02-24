# views.py
from django.shortcuts import render
from .models import Product

def search_view(request):
    """
    Renders the search form.

    This view renders the search form template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered search form template.
    """
    return render(request, 'search_form.html')

def search_results_view(request):
    """
    Renders the search results.

    This view performs a search query based on the provided query parameter
    and renders the search results template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered search results template.
    """
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

def search(request):
    """
    Performs a search query and renders the search results.

    This view handles both GET and POST requests. If the request is a GET
    request, it retrieves the search query from the request parameters and
    performs a search query. If the request is a POST request, it retrieves
    the search query from the form data, performs a search query, and renders
    the search results template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered search results template.
    """
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
    """
    Renders the search form.

    This view renders the search form template, handling both GET and POST
    requests. If the request is a GET request, it initializes a new search
    form. If the request is a POST request, it validates the form data,
    performs a search query, and renders the search results template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered search form template or search results template.
    """
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'form': form, 'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})
