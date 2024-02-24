from django.apps import AppConfig

class CartappConfig(AppConfig):
    """
    AppConfig class for the cartapp app.

    Attributes:
        name (str): The name of the app.
        verbose_name (str): The human-readable name of the app.
    """

    name = 'cartapp'
    verbose_name = 'Cart Application'
