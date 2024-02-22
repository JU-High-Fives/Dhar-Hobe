from django.db import models
from django.utils import timezone

class ProductModel(models.Model):
    """
    Product Model
    =============
    
    Represents a Product to be added by a Renter
    
    Attributes
    ----------
    m_name : str
        The name of the product.
    m_description : str
        A description of the product.
    m_rental_price : float
        The price of the product.
    m_quantity_available : int
        The quantity of the product available in stock.
    m_created_at : datetime
        The date and time when the product was added to the inventory.
    m_updated_at : datetime
        The date and time when the product information was last updated.
    """
    m_name = models.CharField(max_length=255)
    m_description = models.TextField()
    m_rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    m_quantity_available = models.IntegerField(default=0)
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns
        -------
        str
            A string representation of the product.
        """
        return self.m_name

class RenterModel(models.Model):
    """
    Renter Model
    ============

    Represents a renter with a username, password, email, address, and phone number.

    Attributes
    ----------
    m_username : str
        The username of the renter.
    m_password : str
        The password of the renter.
    m_email : str
        The email address of the renter.
    m_address : str
        The address of the renter.
    m_phone_number : str
        The phone number of the renter.
    m_created_at : DateTime
        The date and time when the renter account was created.
    m_updated_at : DateTime
        The date and time when the renter account was last updated.
    """

    m_username = models.CharField(max_length=255)
    m_password = models.CharField(max_length=255)
    m_email = models.EmailField()
    m_address = models.TextField()
    m_phone_number = models.CharField(max_length=20)
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the renter.

        Returns
        -------
        str
            A string representation of the renter.
        """
        return self.m_username

class RenterProductModel(models.Model):
    """
    Renter Product Model
    ====================

    Represents a connection between a renter and a product, indicating that the renter wants to add the product for rent.

    Attributes
    ----------
    m_renter : ForeignKey to RenterModel
        The renter who wants to add the product for rent.
    m_product : ForeignKey to ProductModel
        The product that the renter wants to add for rent.
    m_approved_at : DateTime
        The date and time when the product request was approved.
    """

    m_renter = models.ForeignKey(RenterModel,on_delete=models.CASCADE)
    m_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    m_approved_at = models.DateTimeField(null=True, blank=True)

    IS_APPROVED_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    )
    m_is_approved = models.CharField(max_length=20, choices=IS_APPROVED_CHOICES, default='pending')

    def __str__(self):
        """
        Returns a string representation of the renter product connection.

        Returns
        -------
        str
            A string representation of the renter product connection.
        """
        return "%s %s" % (self.m_renter, self.m_product)

class RenteeModel(models.Model):
    """
    Rentee Model
    ============

    Represents a rentee with a username, password, email, address, and phone number.

    Attributes
    ----------
    m_username : str
        The username of the rentee.
    m_password : str
        The password of the rentee.
    m_email : str
        The email address of the rentee.
    m_address : str
        The address of the rentee.
    m_phone_number : str
        The phone number of the rentee.
    m_created_at : DateTime
        The date and time when the rentee account was created.
    m_updated_at : DateTime
        The date and time when the rentee account was last updated.
    """

    m_username = models.CharField(max_length=255)
    m_password = models.CharField(max_length=255)
    m_email = models.EmailField()
    m_address = models.TextField()
    m_phone_number = models.CharField(max_length=20)
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the renter.

        Returns
        -------
        str
            A string representation of the renter.
        """
        return self.m_username

class ReturnRequestModel(models.Model):
    m_rentee = models.ForeignKey(RenteeModel,on_delete=models.CASCADE)
    m_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    m_approved_at = models.DateTimeField(null=True, blank=True)
    REASON_CHOICES = [
        ('defective', 'Defective'),
        ('damaged', 'Damaged'),
        ('incorrect', 'Incorrect'),
        ('changed_mind', 'Changed Mind'),
    ]

    IS_APPROVED_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    )
    m_is_approved = models.CharField(max_length=20, choices=IS_APPROVED_CHOICES, default='pending')
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)

    def __str__(self):
       
        return "%s %s" % (self.m_rentee, self.m_product)