from django.test import TestCase
from django.urls import reverse
from .models import PaymentModel

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
    
    def test_make_payment_form_valid_submission(self):
        """
        Test a valid form submission in the make_payment view.

        Checks that the form submission redirects to 'payment_success.html' and creates a new payment instance.
        """
        url = reverse('make_payment')
        data = {'order_id': '123', 'amount': 100.00, 'success': True}
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('payment_success'))
        self.assertEqual(PaymentModel.objects.count(), 1)
        payment = PaymentModel.objects.first()
        self.assertEqual(payment.m_order_id, '123')
        self.assertEqual(payment.m_amount, 100.00)
        self.assertTrue(payment.m_success)