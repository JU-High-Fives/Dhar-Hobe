from django.test import TestCase, Client
from django.urls import reverse
from .models import DeliveryRequest
from django.contrib.auth.models import User


class DeliveryRequestViewTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a delivery request for testing
        self.delivery_request = DeliveryRequest.objects.create(
            user=self.user,
            pickup_location='Test Pickup Location',
            delivery_destination='Test Delivery Destination',
            size_weight='Test Size/Weight',
            status='Pending'
        )

    def test_delivery_request_create_view(self):
        # Create a client
        client = Client()

        # Login the client
        client.login(username='testuser', password='testpassword')

        # Get the URL for the delivery request create view
        url = reverse('delivery_request_create')

        # Post data to the view
        response = client.post(url, {
            'pickup_location': 'New Pickup Location',
            'delivery_destination': 'New Delivery Destination',
            'size_weight': 'New Size/Weight',
            'status': 'Pending'  # Make sure to handle the status field properly
        })

        # Check if the request was successful
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect

        # Check if the new delivery request was created
        self.assertTrue(DeliveryRequest.objects.filter(pickup_location='New Pickup Location').exists())

    def test_delivery_request_list_view(self):
        # Create a client
        client = Client()

        # Get the URL for the delivery request list view
        url = reverse('delivery_request_list')

        # Get the response
        response = client.get(url)

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)  # 200 is the status code for a successful GET request

        # Check if the delivery request is present in the response
        self.assertIn(self.delivery_request, response.context['requests'])

    def test_delivery_request_detail_view(self):
        # Create a client
        client = Client()

        # Get the URL for the delivery request detail view
        url = reverse('delivery_request_detail', args=[self.delivery_request.pk])

        # Get the response
        response = client.get(url)

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)  # 200 is the status code for a successful GET request

        # Check if the delivery request details are present in the response
        self.assertEqual(response.context['request'], self.delivery_request)

    def
