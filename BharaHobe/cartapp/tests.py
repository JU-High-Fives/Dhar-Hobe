from django.test import TestCase
from django.urls import reverse
from .models import Product

class SearchViewTests(TestCase):
    def setUp(self):
        # Create some sample products for testing
        Product.objects.create(name='Product 1', description='Description 1')
        Product.objects.create(name='Product 2', description='Description 2')
        Product.objects.create(name='Product 3', description='Description 3')

    def test_search_view(self):
        """
        Test the search view.

        Checks that the view renders the correct template and returns a 200 OK status code.
        """
        url = reverse('search_results')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_search_results(self):
        """
        Test search results with a valid query.

        Checks that the search view returns the correct search results.
        """
        url = reverse('search_results')
        response = self.client.get(url, {'q': 'Product 1'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

        products = response.context['results']
        self.assertEqual(products.count(), 1)
        self.assertEqual(products[0].name, 'Product 1')

    def test_search_results_no_results(self):
        """
        Test search results with no results.

        Checks that the search view returns no results for a non-existent query.
        """
        url = reverse('search_results')
        response = self.client.get(url, {'q': 'Non-existent Product'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

        products = response.context['results']
        self.assertEqual(products.count(), 0)
