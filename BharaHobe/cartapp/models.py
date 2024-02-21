# cartapp/models.py Cart Model

from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id}"
# cartapp/models.py CartItem Model

from django.db import models
from .models import Cart

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# The Cart model includes a foreign key to the User model to associate the cart with a specific user. You can adjust this relationship based on your application's requirements.
# The CartItem model includes foreign keys to the Cart and Product models to link each item to its parent cart and the corresponding product.
    
# ran python manage.py makemigrations and python manage.py migrate commands to create and apply the database migrations. This ensured that the new models are added to your database schema.
