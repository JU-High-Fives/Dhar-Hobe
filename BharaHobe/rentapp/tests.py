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
