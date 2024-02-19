from django.db import models

class PaymentModelManager(models.Manager):
    def search(self, query):
        return self.filter(m_order_id__icontains=query)

class PaymentModel(models.Model):
    m_amount = models.DecimalField(max_digits=10, decimal_places=2)
    m_isSuccess = models.BooleanField(default=False)
    m_order_id = models.CharField(max_length=10, default="")
    m_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    objects = PaymentModelManager()

    def __str__(self):
        """This functions returns the payment id 

        Returns:
            int: Payment ID 
        """
        return f"Payment #{self.id}"
# Perform a search for order IDs containing '123'
results = PaymentModel.objects.search('123')
