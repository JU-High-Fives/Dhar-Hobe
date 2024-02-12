from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class SearchResultsTestCase(TestCase):
    def setUp(self):
        # Create sample products for testing
        Product.objects.create(name='Laptop', category='Electronics', price=1000, location='New York')
        Product.objects.create(name='Chair', category='Furniture', price=50, location='Los Angeles')
        Product.objects.create(name='Tablet', category='Electronics', price=500, location='Chicago')

    def test_search_results_filtered_by_query(self):
        client = Client()
        response = client.get(reverse('search_results'), {'q': 'Laptop'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
        self.assertNotContains(response, 'Chair')
        self.assertNotContains(response, 'Tablet')

    def test_search_results_filtered_by_category(self):
        client = Client()
        response = client.get(reverse('search_results'), {'category': 'Electronics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
        self.assertNotContains(response, 'Chair')
        self.assertContains(response, 'Tablet')

    def test_search_results_filtered_by_price_range(self):
        client = Client()
        response = client.get(reverse('search_results'), {'min_price': 100, 'max_price': 600})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
        self.assertContains(response, 'Tablet')
        self.assertNotContains(response, 'Chair')

    def test_search_results_filtered_by_location(self):
        client = Client()
        response = client.get(reverse('search_results'), {'location': 'New York'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
        self.assertNotContains(response, 'Chair')
        self.assertNotContains(response, 'Tablet')

    def test_no_results_found(self):
        client = Client()
        response = client.get(reverse('search_results'), {'q': 'Non-existent Product'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No results found.')

