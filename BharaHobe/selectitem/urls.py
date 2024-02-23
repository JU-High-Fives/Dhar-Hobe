# Import necessary functions and modules from Django
from django.urls import path
from .views import add_item, select_item 

"""
 Import necessary functions and modules from Django
 Importing view functions from views.py within the same app
 URL patterns for the app
"""
urlpatterns = [

    """
    URL pattern for adding an item
    """
    path('add_item/', add_item, name='add_item'),

    """
     URL pattern for selecting an item
    """
    path('select/', select_item, name='select_item'),
    
    """
     Add other URL patterns as needed...
    """
]

