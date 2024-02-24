from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

@api_view(['POST'])
def add_to_cart(request):
    """
    Add a product to the user's cart.

    This endpoint receives a POST request containing the product ID and optional quantity
    to add the specified product to the user's cart. If the product is already in the cart,
    the quantity is updated accordingly.

    Parameters:
    - request: HTTP request object containing data (product_id, quantity) in the request body.

    Returns:
    - JSON response with the updated cart details.
    """
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
    """
    Retrieve details of the user's cart.

    This endpoint returns details of the user's cart, including the list of items
    and their quantities.

    Parameters:
    - request: HTTP request object.

    Returns:
    - JSON response with the cart details.
    """
    # Retrieve the cart for the current user (you may need to implement user authentication)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Serialize the cart details and return the response
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)
