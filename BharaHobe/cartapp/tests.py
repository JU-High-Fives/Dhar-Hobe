from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from .models import CartItem, Product
from .views import add_to_cart, remove_from_cart

class AddToCartViewTest(TestCase):
    """
    Test case for the add_to_cart view.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()
        self.factory = RequestFactory()
        self.url = reverse('add_to_cart')

    def test_add_to_cart(self):
        """
        Test case to verify the behavior of the add_to_cart view.
        """
        # Create a test product
        product = Product.objects.create(name='Test Product', price=10.0)

        # Create a POST request to the view
        request = self.factory.post(self.url, {'product_id': product.id})
        response = add_to_cart(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Assert that the product is added to the cart
        self.assertTrue(CartItem.objects.filter(product=product).exists())

    def test_add_to_cart_invalid_product(self):
        """
        Test case to verify the behavior of the add_to_cart view with an invalid product ID.
        """
        # Create a POST request to the view with an invalid product ID
        request = self.factory.post(self.url, {'product_id': 999})  # Assuming 999 is not a valid product ID
        response = add_to_cart(request)

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Assert that the cart remains unchanged
        self.assertFalse(CartItem.objects.exists())

class RemoveFromCartViewTest(TestCase):
    """
    Test case for the remove_from_cart view.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()
        self.factory = RequestFactory()
        self.url = reverse('remove_from_cart')

    def test_remove_from_cart(self):
        """
        Test case to verify the behavior of the remove_from_cart view.
        """
        # Create a test product
        product = Product.objects.create(name='Test Product', price=10.0)

        # Add the product to the cart
        cart_item = CartItem.objects.create(product=product, quantity=1)

        # Create a POST request to the view
        request = self.factory.post(self.url, {'product_id': product.id})
        response = remove_from_cart(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Assert that the product is removed from the cart
        self.assertFalse(CartItem.objects.filter(product=product).exists())

    def test_remove_from_cart_invalid_product(self):
        """
        Test case to verify the behavior of the remove_from_cart view with an invalid product ID.
        """
        # Create a POST request to the view with an invalid product ID
        request = self.factory.post(self.url, {'product_id': 999})  # Assuming 999 is not a valid product ID
        response = remove_from_cart(request)

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Assert that the cart remains unchanged
        self.assertFalse(CartItem.objects.exists())
