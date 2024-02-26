from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    """
    Model representing a user's shopping cart.

    Attributes:
        user (User): The user who owns the cart.
        created_at (DateTimeField): The date and time when the cart was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the cart.

        Returns:
            str: A string representation of the cart.
        """
        return f"Cart #{self.id}"

class CartItem(models.Model):
    """
    Model representing an item in a user's shopping cart.

    Attributes:
        cart (Cart): The cart to which this item belongs.
        product (Product): The product associated with this item.
        quantity (PositiveIntegerField): The quantity of the product in the cart.
        created_at (DateTimeField): The date and time when the cart item was created.
    """
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the cart item.

        Returns:
            str: A string representation of the cart item.
        """
        return f"{self.quantity} x {self.product.name}"
