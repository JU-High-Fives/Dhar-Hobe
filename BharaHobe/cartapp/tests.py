from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Cart

class AddToCartIntegrationTest(TestCase):
    def setUp(self):
        # Create a test user (optional)
        self.user = User.objects.create(username='test_user')

        # Create a test product
        self.product = Product.objects.create(name='Test Product', price=100)

    def test_add_to_cart(self):
        client = Client()

        # Simulate adding the product to the cart
        response = client.post(reverse('add_to_cart'), {'product_id': self.product.id}, follow=True)

        # Check if the product was added successfully
        self.assertEqual(response.status_code, 200)

        # Check if the cart contains the added product
        cart_items = Cart.objects.filter(user=self.user)
        self.assertTrue(cart_items.exists())
        self.assertEqual(cart_items.first().product, self.product)

    def test_add_to_cart_invalid_product(self):
        client = Client()

        # Simulate adding an invalid product to the cart
        response = client.post(reverse('add_to_cart'), {'product_id': 999}, follow=True)

        # Check if the response indicates failure
        self.assertEqual(response.status_code, 404)

        # Check if the cart remains empty
        cart_items = Cart.objects.filter(user=self.user)
        self.assertFalse(cart_items.exists())
