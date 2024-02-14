from django.shortcuts import render
from .models import Product

def search_results_view(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')
    
    # Start with all products
    results = Product.objects.all()
    
    # Filter by search query
    if query:
        results = results.filter(name__icontains=query)
    
    # Filter by category
    if category:
        results = results.filter(category=category)
    
    # Filter by price range
    if min_price:
        results = results.filter(price__gte=min_price)
    if max_price:
        results = results.filter(price__lte=max_price)
    
    # Filter by location
    if location:
        results = results.filter(location__icontains=location)

    if query:
        # Perform keyword-based search
        results = Product.objects.filter(name__icontains=query) | \
                  Product.objects.filter(description__icontains=query)
    else:
        results = []
    return render(request, 'search_results.html', {'results': results, 'query': query})
    


# In this backend logic:

#     We extract the filtering criteria (e.g., query, category, min_price, max_price, location) from the request parameters using request.GET.get().
#     We start with all products (Product.objects.all()) and apply filters based on the provided criteria using queryset filtering methods.
#     Finally, we pass the filtered queryset (results) and the search query (query) to the template for rendering.

# The search_view function extracts the search query from the request parameters and performs a keyword-based search against the name and description fields of the Product model using the icontains lookup.
