from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
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
    
    def test_initiate_return_request_post_valid_form(self):
        """
        Test POST request with valid form for initiate_return_request view.
        """
        url = reverse('initiate_return_request', args=[self.item.pk])
        form_data = {'reason': 'defective', 'desired_resolution': 'refund', 'supporting_evidence': 'Evidence'}
        self.client.force_login(self.user)
        response = self.client.post(url, form_data)
        self.assertRedirects(response, reverse('return_request_confirmation'))  # Use reverse to get the URL
        self.assertTrue(ReturnRequest.objects.filter(user=self.user, item=self.item, reason='defective').exists())

    def test_return_request_confirmation(self):
        """
        Test return_request_confirmation view.
        """
        url = reverse('return_request_confirmation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
