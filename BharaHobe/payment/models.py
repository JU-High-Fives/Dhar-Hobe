from django.db import models

class OrderModel(models.Model):
    """
    Model representing an order.
    """
    m_order_id = models.AutoField(primary_key=True)
    m_items = models.TextField()
    m_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    m_notes = models.TextField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        """
        Constructor for OrderModel.

        Initializes the monthly payment amount based on the total amount.
        """
        super(OrderModel, self).__init__(*args, **kwargs)
        if self.m_total_amount:
            self.m_monthly_pay = self.m_total_amount // 6
        else:
            self.m_monthly_pay = 0

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return f"Order #{self.m_order_id}"

class PaymentModel(models.Model):
    """
    Model representing a payment for an order.
    """
    m_order_id = models.CharField(max_length=50)
    m_amount = models.DecimalField(max_digits=10, decimal_places=2)
    m_isSuccess = models.BooleanField(default=False)
    m_payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default="")
    m_notes = models.TextField(blank=True, null=True)
    m_card_token = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the payment.
        """
        return f"Payment #{self.id}"
