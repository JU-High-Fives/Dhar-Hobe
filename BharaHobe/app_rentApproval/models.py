from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Product
    =======
    
    Represents a Product to be added by a Renter
    
    Attributes
    ----------
    name : str
        The name of the product.
    description : str
        A description of the product.
    price : float
        The price of the product.
    quantity_available : int
        The quantity of the product available in stock.
    created_at : datetime
        The date and time when the product was added to the inventory.
    updated_at : datetime
        The date and time when the product information was last updated.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns
        -------
        str
            A string representation of the product.
        """
        return self.name

class Renter(models.Model):
    """
    Renter Model
    ============

    Represents a renter with a username, password, email, address, and phone number.

    Attributes
    ----------
    username : str
        The username of the renter.
    password : str
        The password of the renter.
    email : str
        The email address of the renter.
    address : str
        The address of the renter.
    phone_number : str
        The phone number of the renter.
    created_at : DateTime
        The date and time when the renter account was created.
    updated_at : DateTime
        The date and time when the renter account was last updated.
    """

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the renter.

        Returns
        -------
        str
            A string representation of the renter.
        """
        return self.username

class RenterProduct(models.Model):
    """
    Renter Product Model
    ====================

    Represents a connection between a renter and a product, indicating that the renter wants to add the product for rent.

    Attributes
    ----------
    renter : ForeignKey to Renter
        The renter who wants to add the product for rent.
    product : ForeignKey to Product
        The product that the renter wants to add for rent.
    

    """
    renter = models.ForeignKey(Renter,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        """
        Returns a string representation of the renter product connection.

        Returns
        -------
        str
            A string representation of the renter product connection.
        """
                
        return "%s %s" % (self.renter, self.product)