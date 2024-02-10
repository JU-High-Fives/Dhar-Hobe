from django.test import TestCase, RequestFactory,Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Renter, Product, RenterProduct
from .views import add_product_rqsts
from .views import admin_page

class AddProductRqstsViewTestCase(TestCase):
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
        self.assertContains(response, 'No products available for rent.')
        
class AdminPageViewTestCase(TestCase):
    """
    Test case for the admin_page view.
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
    
