from django.test import TestCase, RequestFactory,Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Renter, Product, RenterProduct
from .views import *
from .views import admin_page
from .services import EmailService,ProductService

class AddProductRqstsViewTest(TestCase):
    """
    Test case for the add_product_rqsts view.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.factory = RequestFactory()
        self.url = reverse('add_product_rqsts')

    def test_add_product_rqsts(self):
        """
        Test case to verify the behavior of the add_product_rqsts view when products are available for rent.
        """
        renter = Renter.objects.create(username='testuser', password='testpassword', email='test@example.com',
                                       address='Test Address', phone_number='1234567890')
        product1 = Product.objects.create(name='Product 1', description='Description 1', rental_price=10.0,
                                          quantity_available=5)
        product2 = Product.objects.create(name='Product 2', description='Description 2', rental_price=15.0,
                                          quantity_available=8)
        
        RenterProduct.objects.create(renter=renter, product=product1)
        RenterProduct.objects.create(renter=renter, product=product2)

        # Create a GET request to the view
        request = self.factory.get(self.url)
        request.user = renter
        response = add_product_rqsts(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')

    def test_add_product_rqsts_with_no_products(self):
        """
        Test case to verify the behavior of the add_product_rqsts view when no products are available for rent.
        """
        # Create a test renter
        renter = Renter.objects.create(username='testuser', password='testpassword', email='test@example.com',
                                       address='Test Address', phone_number='1234567890')

        # Create a GET request to the view
        request = self.factory.get(self.url)

        # Associate the test renter with the request (simulate authentication)
        request.user = renter

        # Call the view function and get the response
        response = add_product_rqsts(request)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains a message indicating no products are available
        self.assertContains(response, 'No add products requests for rent is available')
        
class AdminPageViewTest(TestCase):
    """
    Test case for the admin_page view .
    """
    def setUp(self):
        # Set up the test client
        self.client = Client()
        self.url = reverse('admin_page')  # Assuming 'admin_page' is the URL name for the view

    def test_admin_page_view(self):
        # Create a GET request to the view using the test client
        response = self.client.get(self.url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used for rendering the response
        self.assertTemplateUsed(response, 'app_rentApproval/admin_page.html')

class ApproveProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.renter = Renter.objects.create(username='testuser', email='test@example.com')
        self.product = Product.objects.create(name='Test Product', rental_price=10.0)
        self.renter_product = RenterProduct.objects.create(renter=self.renter, product=self.product, is_approved='pending')

    def test_approve_product(self):
        url = reverse('approve_product', kwargs={'request_id': self.renter_product.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.renter_product.refresh_from_db()
        self.assertEqual(self.renter_product.is_approved, 'approved')
    
class DisapproveProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.renter = Renter.objects.create(username='testuser', email='test@example.com')
        self.product = Product.objects.create(name='Test Product', rental_price=10.0)
        self.renter_product = RenterProduct.objects.create(renter=self.renter, product=self.product, is_approved='pending')

    def test_disapprove_product(self):
        url = reverse('disapprove_product', kwargs={'request_id': self.renter_product.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.renter_product.refresh_from_db()
        self.assertEqual(self.renter_product.is_approved, 'disapproved')

class ApprovedRequestsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_approved_requests(self):
        # Create approved renter product requests
        renter1 = Renter.objects.create(username='testuser1', email='test1@example.com')
        product1 = Product.objects.create(name='Product 1', rental_price=10.0)
        approved_request1 = RenterProduct.objects.create(renter=renter1, product=product1, is_approved='approved')

        renter2 = Renter.objects.create(username='testuser2', email='test2@example.com')
        product2 = Product.objects.create(name='Product 2', rental_price=15.0)
        approved_request2 = RenterProduct.objects.create(renter=renter2, product=product2, is_approved='approved')

        request = self.factory.get(reverse('approved_requests'))
        response = approved_requests(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertNotContains(response, 'No approved requests')

class DisapprovedRequestsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_disapproved_requests(self):
        # Create disapproved renter product requests
        renter1 = Renter.objects.create(username='testuser1', email='test1@example.com')
        product1 = Product.objects.create(name='Product 1', rental_price=10.0)
        disapproved_request1 = RenterProduct.objects.create(renter=renter1, product=product1, is_approved='disapproved')

        renter2 = Renter.objects.create(username='testuser2', email='test2@example.com')
        product2 = Product.objects.create(name='Product 2', rental_price=15.0)
        disapproved_request2 = RenterProduct.objects.create(renter=renter2, product=product2, is_approved='disapproved')

        request = self.factory.get(reverse('disapproved_requests'))
        response = disapproved_requests(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertNotContains(response, 'No disapproved requests')