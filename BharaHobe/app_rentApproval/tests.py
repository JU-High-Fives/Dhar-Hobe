from django.test import TestCase, RequestFactory,Client
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch

from .models import RenterModel, ProductModel, RenterProductModel,RenteeModel,ReturnRequestModel
from .views import *
from .views import admin_page
from .services import EmailService,ProductService,ReturnService

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
        renter = RenterModel.objects.create(m_username='testuser', m_password='testpassword', m_email='test@example.com',
                                       m_address='Test Address', m_phone_number='1234567890')
        product1 = ProductModel.objects.create(m_name='Product 1', m_description='Description 1', m_rental_price=10.0,
                                          m_quantity_available=5)
        product2 = ProductModel.objects.create(m_name='Product 2', m_description='Description 2', m_rental_price=15.0,
                                          m_quantity_available=8)
        
        RenterProductModel.objects.create(m_renter=renter, m_product=product1)
        RenterProductModel.objects.create(m_renter=renter, m_product=product2)

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
        renter = RenterModel.objects.create(m_username='testuser', m_password='testpassword', m_email='test@example.com',
                                       m_address='Test Address', m_phone_number='1234567890')

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
    """
    Test case for the approve_product view.

    This test case checks the behavior of the approve_product view function.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()
        self.renter = RenterModel.objects.create(m_username='testuser', m_email='test@example.com')
        self.product = ProductModel.objects.create(m_name='Test Product', m_rental_price=10.0)
        self.renter_product = RenterProductModel.objects.create(m_renter=self.renter, m_product=self.product, m_is_approved='pending')

    def test_approve_product(self):
        """
        Test case to verify the behavior of the approve_product view.

        This test case sends a POST request to the view to approve a product request,
        checks if the response is a redirect, and verifies that the product request's
        approval status is updated to 'approved'.
        """
        url = reverse('approve_product', kwargs={'request_id': self.renter_product.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.renter_product.refresh_from_db()
        self.assertEqual(self.renter_product.m_is_approved, 'approved')
    
class DisapproveProductViewTest(TestCase):
    """
    Test case for the disapprove_product view.

    This test case checks the behavior of the disapprove_product view function.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()
        self.renter = RenterModel.objects.create(m_username='testuser', m_email='test@example.com')
        self.product = ProductModel.objects.create(m_name='Test Product', m_rental_price=10.0)
        self.renter_product = RenterProductModel.objects.create(m_renter=self.renter, m_product=self.product, m_is_approved='pending')

    def test_disapprove_product(self):
        """
        Test case to verify the behavior of the disapprove_product view.

        This test case sends a POST request to the view to disapprove a product request,
        checks if the response is a redirect, and verifies that the product request's
        approval status is updated to 'disapproved'.
        """
        url = reverse('disapprove_product', kwargs={'request_id': self.renter_product.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.renter_product.refresh_from_db()
        self.assertEqual(self.renter_product.m_is_approved, 'disapproved')

class ApprovedRequestsViewTest(TestCase):
    """
    Test case for the approved_requests view.

    This test case checks the behavior of the approved_requests view function.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.factory = RequestFactory()

    def test_approved_requests(self):
        """
        Test case to verify the behavior of the approved_requests view.

        This test case creates approved product requests, sends a GET request to the view,
        and asserts that the response contains the expected approved product requests.
        """
        # Create approved renter product requests
        renter1 = RenterModel.objects.create(m_username='testuser1', m_email='test1@example.com')
        product1 = ProductModel.objects.create(m_name='Product 1', m_rental_price=10.0)
        approved_request1 = RenterProductModel.objects.create(m_renter=renter1, m_product=product1, m_is_approved='approved')

        renter2 = RenterModel.objects.create(m_username='testuser2', m_email='test2@example.com')
        product2 = ProductModel.objects.create(m_name='Product 2', m_rental_price=15.0)
        approved_request2 = RenterProductModel.objects.create(m_renter=renter2, m_product=product2, m_is_approved='approved')

        request = self.factory.get(reverse('approved_requests'))
        response = approved_requests(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertNotContains(response, 'No approved requests')

class DisapprovedRequestsViewTest(TestCase):
    """
    Test case for the disapproved_requests view.

    This test case checks the behavior of the disapproved_requests view function.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.factory = RequestFactory()

    def test_disapproved_requests(self):
        """
        Test case to verify the behavior of the disapproved_requests view.

        This test case creates disapproved product requests, sends a GET request to the view,
        and asserts that the response contains the expected disapproved product requests.
        """
        # Create disapproved renter product requests
        renter1 = RenterModel.objects.create(m_username='testuser1', m_email='test1@example.com')
        product1 = ProductModel.objects.create(m_name='Product 1', m_rental_price=10.0)
        disapproved_request1 = RenterProductModel.objects.create(m_renter=renter1, m_product=product1, m_is_approved='disapproved')

        renter2 = RenterModel.objects.create(m_username='testuser2', m_email='test2@example.com')
        product2 = ProductModel.objects.create(m_name='Product 2', m_rental_price=15.0)
        disapproved_request2 = RenterProductModel.objects.create(m_renter=renter2, m_product=product2, m_is_approved='disapproved')

        request = self.factory.get(reverse('disapproved_requests'))
        response = disapproved_requests(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertNotContains(response, 'No disapproved requests')



#------------------------------------------------------------------------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Sprint2 testing
class ReturnRequestViewTest(TestCase):
    """
    Test case for the view handling return requests.

    Attributes:
        factory (RequestFactory): An instance of RequestFactory for creating mock requests.
        url (str): The URL of the return requests view.
    """
    def setUp(self):
        """
        Set up method to initialize common resources for testing.
        """
        self.factory = RequestFactory()
        self.url = reverse('return_requests')

    def test_return_requests(self):
        """
        Test case to check if return requests are displayed correctly.

        Creates mock rentee, products, and return requests.
        Verifies that the view displays the return requests correctly.
        """
        rentee = RenteeModel.objects.create(m_username='testuser', m_password='testpassword', m_email='test@example.com',
                                       m_address='Test Address', m_phone_number='1234567890')
        product1 = ProductModel.objects.create(m_name='Product 1', m_description='Description 1', m_rental_price=10.0,
                                          m_quantity_available=5)
        product2 = ProductModel.objects.create(m_name='Product 2', m_description='Description 2', m_rental_price=15.0,
                                          m_quantity_available=8)
        
        ReturnRequestModel.objects.create(m_rentee=rentee, m_product=product1)
        ReturnRequestModel.objects.create(m_rentee=rentee, m_product=product2)

        # Create a GET request to the view
        request = self.factory.get(self.url)
        request.user = rentee
        response = return_requests(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')

    def test_return_requests_with_no_products(self):
        """
        Test case to check behavior when no return requests are available.

        Creates a mock rentee.
        Verifies that the view displays a message when no return requests are available.
        """
        rentee = RenteeModel.objects.create(m_username='testuser', m_password='testpassword', m_email='test@example.com',
                                       m_address='Test Address', m_phone_number='1234567890')
        request = self.factory.get(self.url)
        request.user = rentee
        response = return_requests(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No return requests for product is available')






