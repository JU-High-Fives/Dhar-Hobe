from django.db import models

class OrderModel(models.Model):
    m_order_id = models.CharField(max_length=50, unique=True)
    m_items = models.TextField()
    m_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    m_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        """This function returns the order ID for better readability.

        Returns:
            str: Order ID
        """
        return f"Order #{self.m_order_id}"
    
class PaymentModel(models.Model):
    m_order_id = models.CharField(max_length=50)
    m_amount = models.DecimalField(max_digits=10, decimal_places=2)
    m_isSuccess = models.BooleanField(default=False)
    m_payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default = "")
    m_notes = models.TextField(blank=True, null=True)
    def __str__(self):
        """This functions returns the payment id 

        Returns:
            int: Payment ID 
        """
        return f"Payment #{self.id}"