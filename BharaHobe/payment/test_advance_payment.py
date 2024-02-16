from django.test import TestCase
from .forms import advancePaymentForm
from django.core.exceptions import ValidationError


class TestAdvancePaymentForm(TestCase):
    def setUp(self):
        """Set up common data for the test cases."""
        self.valid_credit_card_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '4111125634596325',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }
        self.invalid_credit_card_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '000000000',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

    def test_valid_credit_card(self):
        """Test form validation for a valid credit card."""
        form = advancePaymentForm(data=self.valid_credit_card_data)
        with self.assertRaises(ValidationError) as context:
            form.full_clean()

        expected_error_message = 'Invalid credit card number'
        self.assertEqual(str(context.exception), expected_error_message)

    def test_invalid_credit_card(self):
        """Test form validation for an invalid credit card."""
        form = advancePaymentForm(data=self.invalid_credit_card_data)
        with self.assertRaises(ValidationError) as context:
            form.full_clean()

        expected_error_message = 'Invalid credit card number'
        self.assertEqual(str(context.exception), expected_error_message)

    def test_no_duplicate_payment(self):
        """Test that no duplicate payment is allowed."""
        form_data = {
            'f_payment_method': 'paypal',
            'f_credit_card_number': '4111125634596325',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

        form = advancePaymentForm(data=form_data)
        form.full_clean()

        with self.assertRaises(ValidationError) as context:
            form = advancePaymentForm(data=form_data)
            form.full_clean()

        expected_error_message = 'Payment with this Credit Card/PayPal Number already exists.'
        self.assertEqual(str(context.exception), expected_error_message)


if __name__ == '__main__':
    import unittest
    unittest.main()
