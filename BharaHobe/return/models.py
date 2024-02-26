from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    """
    Model representing an item in the system.

    Fields:
        m_name (CharField): The name of the item.
        m_description (TextField): Description of the item.
        m_price (DecimalField): Price of the item.
        Add other fields as needed for the item.
    """
    m_name = models.CharField(max_length=100)
    m_description = models.TextField()
    m_price = models.DecimalField(max_digits=10, decimal_places=2)

class ReturnRequest(models.Model):
    """
    Model representing a return request for an item.

    Fields:
        REASON_CHOICES (list of tuples): Choices for reasons for return.
        STATUS_CHOICES (list of tuples): Choices for status of the return request.
        user (ForeignKey): The user who initiated the return request.
        item (ForeignKey): The item for which return is requested.
        reason (CharField): Reason for return.
        desired_resolution (CharField): Desired resolution by the user.
        supporting_evidence (TextField): Any supporting evidence provided by the user.
        status (CharField): Status of the return request.
        created_at (DateTimeField): Date and time when the return request was created.
        updated_at (DateTimeField): Date and time when the return request was last updated.
    """
    REASON_CHOICES = [
        ('defective', 'Defective'),
        ('damaged', 'Damaged'),
        ('incorrect', 'Incorrect'),
        ('changed_mind', 'Changed Mind'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    m_user = models.ForeignKey(User, on_delete=models.CASCADE)
    m_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    m_reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    m_desired_resolution = models.CharField(max_length=20)
    m_supporting_evidence = models.TextField()
    m_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_updated_at = models.DateTimeField(auto_now=True)
