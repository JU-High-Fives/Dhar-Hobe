from django.test import TestCase
from django.urls import reverse
from .models import Item

class SelectItemIntegrationTestCase(TestCase):
    def setUp(self):
        # Create sample items for testing
        self.item1 = Item.objects.create(name='Item 1', description='Description for Item 1')
        self.item2 = Item.objects.create(name='Item 2', description='Description for Item 2')

    def test_select_item_view_get(self):
        # Testing the GET request to the select_item view
        response = self.client.get(reverse('select_item'))
        
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)
        
        # Check if the correct template is rendered
        self.assertTemplateUsed(response, 'additem/select_item.html')

        # Ensure that both items are present in the response context
        self.assertIn(self.item1, response.context['form'].fields['item'].queryset)
        self.assertIn(self.item2, response.context['form'].fields['item'].queryset)

    def test_select_item_view_post_valid(self):
        # Testing the POST request to the select_item view with valid data
        data = {'item': self.item1.id}  # Simulate selecting item1
        response = self.client.post(reverse('select_item'), data)
        
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)
        
        # Check if the correct template is rendered
        self.assertTemplateUsed(response, 'additem/selected_item.html')
        
        # Check if the selected item is rendered in the response
        self.assertContains(response, 'Item 1')

    def test_select_item_view_post_invalid(self):
        # Testing the POST request to the select_item view with invalid data
        data = {}  # Missing 'item' field
        response = self.client.post(reverse('select_item'), data)
        
        # Check if the response status code is not 200 (indicating failure)
        self.assertNotEqual(response.status_code, 200)
        
        # Ensure that the response contains an error message or redirects to another page
        # Depending on your project's behavior for invalid form submissions
        
        # Example: Check if the response redirects to the select_item page again
        self.assertRedirects(response, reverse('select_item'))
