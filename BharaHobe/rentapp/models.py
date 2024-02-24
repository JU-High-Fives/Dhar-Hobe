from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.name
    
    # We write test methods to test specific aspects of the Product model, such as its __str__ method and attribute values.

    class Meta:
        app_label = 'rentapp'
