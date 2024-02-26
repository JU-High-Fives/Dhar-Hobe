from django.test import TestCase
from .forms import monthlyPaymentForm
from .models import OrderModel
from decimal import Decimal


class TestMonthlyPaymentForm(TestCase):
    """
    Test cases for the Monthly Payment Form.

    Attributes:
        valid_monthly_payment_data (MonthlyPaymentForm): Valid form data for monthly payment.
        invalid_monthly_payment_data (MonthlyPaymentForm): Invalid form data for monthly payment.

    Methods:
        setUp: Sets up common data for the test cases.
        test_valid_monthly_payment: Test form validation for valid monthly payment data.
        test_invalid_monthly_payment: Test form validation for invalid monthly payment data.
        test_duplicate_payment: Test for attempting to make a duplicate monthly payment.
    """

    def setUp(self):
        """Set up common data for the test cases."""
        self.valid_monthly_payment_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '4111125634596325',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }
        self.invalid_monthly_payment_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '0000',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }
        self.form_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '4111125634596325',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

    def test_valid_monthly_payment(self):
        """Test form validation for valid monthly payment data."""
        form = monthlyPaymentForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['f_card_token'], 'mock_card_token')

    def test_duplicate_payment(self):
        """Test for attempting to make a duplicate monthly payment."""
        response = self.client.post('/monthly_payment_form/1', data=self.valid_monthly_payment_data)
        self.assertEqual(response.status_code, 404)
    
    def test_deduct_amount_after_successful_payment(self):
        """Test deducting amount after a successful monthly payment."""
        initial_amount = 500.00
        order = OrderModel.objects.create(m_order_id='123', m_items='Test Item', m_total_amount=initial_amount)
        response = self.client.post('/monthly_payment_form/1', data=self.valid_monthly_payment_data)
        self.assertEqual(response.status_code, 200)
        order.refresh_from_db()
        expected_amount = initial_amount - Decimal(self.valid_monthly_payment_data['f_amount'])
        self.assertEqual(order.m_total_amount, expected_amount)


if __name__ == '__main__':
    import unittest
    unittest.main()
