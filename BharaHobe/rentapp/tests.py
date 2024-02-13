# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product
from .forms import SearchForm

class ProductSearchTestCase(TestCase):
    def setUp(self):
        # Create some sample products for testing
        Product.objects.create(name='Product 1', description='Description 1')
        Product.objects.create(name='Product 2', description='Description 2')
        Product.objects.create(name='Product 3', description='Description 3')

    def test_search_form_rendered_correctly(self):
        client = Client()
        response = client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], SearchForm)

    def test_search_results(self):
        client = Client()
        response = client.get(reverse('search_results'), {'query': 'Product 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')  # Ensure that 'Product 1' is present in the response content
        self.assertNotContains(response, 'Product 2')  # Ensure that 'Product 2' is not present in the response content

from django.test import TestCase
from myapp.models import Product

class ProductModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test data for the model
        Product.objects.create(name='Laptop', category='Electronics', price=999.99)

    def test_product_str_method(self):
        # Test the __str__ method of the Product model
        laptop = Product.objects.get(name='Laptop')
        self.assertEqual(str(laptop), 'Laptop')

    def test_product_attributes(self):
        # Test the attributes of the Product model
        laptop = Product.objects.get(name='Laptop')
        self.assertEqual(laptop.name, 'Laptop')
        self.assertEqual(laptop.category, 'Electronics')
        self.assertEqual(laptop.price, 999.99)

    # We created a ProductModelTestCase class that inherits from django.test.TestCase.
    # We defined a setUpTestData class method to set up test data (in this case, a product instance) before running the tests.
    # We wrote test methods to test specific aspects of the Product model, such as its __str__ method and attribute values.
