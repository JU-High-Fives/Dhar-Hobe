# File: myapp/tests.py

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Item, ReturnRequest
from .views import initiate_return_request, return_request_confirmation
from .forms import ReturnRequestForm

class TestReturnRequestViews(TestCase):
    """
    Test cases for return request views.
    """

    def setUp(self):
        """
        Setup method to create common data for test cases.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.item = Item.objects.create(name='Test Item', description='Description', price=10.00)
    
    def test_initiate_return_request_get(self):
        """
        Test GET request for initiate_return_request view.
        """
        request = self.factory.get('/return/1/')
        request.user = self.user
        response = initiate_return_request(request, self.item.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_initiate_return_request_post_valid_form(self):
        """
        Test POST request with valid form for initiate_return_request view.
        """
        request = self.factory.post('/return/1/', {'reason': 'defective', 'desired_resolution': 'refund', 'supporting_evidence': 'Evidence'})
        request.user = self.user
        response = initiate_return_request(request, self.item.pk)
        self.assertRedirects(response, '/return_request_confirmation/')
        self.assertTrue(ReturnRequest.objects.filter(user=self.user, item=self.item, reason='defective').exists())

    def test_initiate_return_request_post_invalid_form(self):
        """
        Test POST request with invalid form for initiate_return_request view.
        """
        request = self.factory.post('/return/1/', {})
        request.user = self.user
        response = initiate_return_request(request, self.item.pk)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ReturnRequest.objects.filter(user=self.user, item=self.item).exists())

    def test_return_request_confirmation(self):
        """
        Test return_request_confirmation view.
        """
        request = self.factory.get('/return_request_confirmation/')
        response = return_request_confirmation(request)
        self.assertEqual(response.status_code, 200)
