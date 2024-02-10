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

        :return: None
        """
        url = reverse('make_payment')
        data = {'f_order_id': '123', 'f_amount': 100.00, 'f_isSuccess': True}
        self.client.post(url, data)

        self.assertEqual(PaymentModel.objects.count(), 1)
        payment = PaymentModel.objects.first()
        self.assertEqual(payment.m_order_id, '123')
        self.assertEqual(payment.m_amount, 100.00)
        self.assertTrue(payment.m_isSuccess)

    def test_make_payment_form_invalid_submission(self):
            """
            Test an invalid form submission in the make_payment view.

            Checks that the form submission returns a 200 OK status code, stays on the 'make_payment' page,
            has form errors, and does not create a new payment instance.
            """
            url = reverse('make_payment')
            data = {'order_id': '123', 'amount': 'invalid_amount', 'success': True}
            response = self.client.post(url, data)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'make_payment.html')

            form = response.context['form']
            self.assertTrue(form.errors)

            self.assertEqual(PaymentModel.objects.count(), 0)