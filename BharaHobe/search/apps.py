# apps.py
from django.apps import AppConfig

class SearchConfig(AppConfig):
    """
    AppConfig for the search app.

    This class defines the configuration for the search app, including its
    name and verbose name.

    Attributes:
        name (str): The name of the app.
        verbose_name (str): The human-readable name of the app.
    """

    name = 'search'
    verbose_name = 'Search'
