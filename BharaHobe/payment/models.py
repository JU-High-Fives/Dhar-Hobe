from django.db import models

class PaymentModel(models.Model):
    m_amount = models.DecimalField(max_digits=10, decimal_places=2)
    m_isSuccess = models.BooleanField(default=False)
    m_order_id = models.CharField(max_length = 10, default = "")
    m_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"Payment #{self.id}"
