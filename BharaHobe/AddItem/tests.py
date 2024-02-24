from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item
from .views import add_item
from .forms import ItemForm

class AddItemTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword')

    def test_add_item_success(self):

        """
        Test if adding item is successful with valid data
        Define valid item data
        """
        
        
        item_data = {
            'name': 'Test Item',
            'description': 'This is a test item',
        }

        """
         Create a POST request
        """
        request = self.factory.post(reverse('add_item'), data=item_data)
        request.user = self.user
        
        """
         Call the add_item view function
        """
        response = add_item(request)

        """
         Check if the item was added successfully (status code 302 indicates redirect)
        """
        self.assertEqual(response.status_code, 302)

        """
         Check if the item exists in the database
        """
        self.assertTrue(Item.objects.filter(name='Test Item').exists())

    def test_add_item_failure_missing_info(self):

        """
        Test if adding item fails when required details are missing
         Define incomplete item data
        """
        
        incomplete_item_data = {
            'name': 'Incomplete Item',

            """
             'description' is intentionally missing
            """
        }

        """
         Create a POST request
        """
        request = self.factory.post(reverse('add_item'), data=incomplete_item_data)
        request.user = self.user

        """
         Call the add_item view function

        """
        response = add_item(request)

        """
        Check if the form was not submitted successfully (status code 200 indicates failure)
        """
        self.assertEqual(response.status_code, 200)

        """
         Check if the error message is displayed in the response content
        """
        self.assertContains(response, "This field is required.")

    def test_add_item_failure_invalid_data(self):

        """
        Test if adding item fails with invalid data
        Define invalid item data (empty data)
        """
        
        invalid_item_data = {}

        """
             Create a POST request
        """
        request = self.factory.post(reverse('add_item'), data=invalid_item_data)
        request.user = self.user

        """
        Call the add_item view function
        """
        response = add_item(request)

        """
         Check if the form was not submitted successfully (status code 200 indicates failure)
        """
        self.assertEqual(response.status_code, 200)

        """
         Check if the error message is displayed in the response content
        """
        self.assertContains(response, "This field is required.")
