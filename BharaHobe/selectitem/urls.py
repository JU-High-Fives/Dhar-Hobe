from django.urls import path
from .views import select_item, process_selection

"""
Defines URL patterns for the selectitem app.
"""


urlpatterns = [

    """
    URL pattern for selecting an item
    """
    path('', select_item, name='select_item'),

"""
 URL pattern for processing the selected item
"""
    path('process/', process_selection, name='process_selection'),
]
