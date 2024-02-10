from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    success = models.BooleanField(default=False)
    order_id = models.CharField(max_length = 10, default = "")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"Payment #{self.id}"
