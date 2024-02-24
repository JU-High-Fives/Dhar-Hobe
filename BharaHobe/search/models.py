from django.db import models

class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name (str): The name of the product.
        category (str): The category of the product.
        price (Decimal): The price of the product.
        location (str): The location where the product is located.
        description (str): A description of the product.
    """

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.name
