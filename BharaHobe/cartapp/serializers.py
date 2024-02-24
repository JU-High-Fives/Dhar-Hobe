from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for the CartItem model.

    This serializer is used to serialize CartItem objects, providing JSON representations
    of cart items with the specified fields.

    Attributes:
        id (IntegerField): The unique identifier for the cart item.
        product (PrimaryKeyRelatedField): The associated product for the cart item.
        quantity (IntegerField): The quantity of the product in the cart item.
    """

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Cart model.

    This serializer is used to serialize Cart objects, providing JSON representations
    of carts with the specified fields and nested cart item data.

    Attributes:
        id (IntegerField): The unique identifier for the cart.
        user (PrimaryKeyRelatedField): The user associated with the cart.
        created_at (DateTimeField): The date and time when the cart was created.
        cart_items (CartItemSerializer): A nested serializer for cart items associated with the cart.
    """

    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'cart_items']
