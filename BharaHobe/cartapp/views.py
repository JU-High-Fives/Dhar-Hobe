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
# cartapp/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

@api_view(['POST'])
def add_to_cart(request):
    # Get data from request
    data = request.data
    
    # Assuming the request contains product_id and quantity
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)  # Default quantity is 1
    
    # Retrieve the cart for the current user (you may need to implement user authentication)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
    
    # If the product is already in the cart, update the quantity
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    else:
        cart_item.quantity = quantity
        cart_item.save()
    
    # Serialize the updated cart and return the response
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_cart_details(request):
    # Retrieve the cart for the current user (you may need to implement user authentication)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Serialize the cart details and return the response
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

