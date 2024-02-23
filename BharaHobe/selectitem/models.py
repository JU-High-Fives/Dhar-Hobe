from django.db import models

class Item(models.Model):
    """
    Represents an item available for renting.
    
    Attributes:
        name (str): The name of the item.
        description (str): A brief description of the item.
    """
    name = models.CharField(max_length=100, help_text="Enter the name of the item")
    description = models.TextField(help_text="Enter a brief description of the item")

    def __str__(self):
        """
        Return a string representation of the item.
        """
        return self.name
