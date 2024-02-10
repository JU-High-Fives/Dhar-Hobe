from django.test import TestCase
from django.urls import reverse

class PaymentViewTests(TestCase):
    def test_make_payment_view(self):
        """
        Test the make_payment view.

        Checks that the view renders the correct template and returns a 200 OK status code.
        """
        url = reverse('make_payment')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'make_payment.html')