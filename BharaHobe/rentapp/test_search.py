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



# In these test cases:

#     setUp: Creates sample products for testing.
#     test_search_results_filtered_by_query: Tests if search results are filtered correctly by the search query.
#     test_search_results_filtered_by_category: Tests if search results are filtered correctly by category.
#     test_search_results_filtered_by_price_range: Tests if search results are filtered correctly by price range.
#     test_search_results_filtered_by_location: Tests if search results are filtered correctly by location.
#     test_no_results_found: Tests the scenario when no results are found for the given query.

# These test cases simulate different scenarios and verify that the search functionality works as expected.

