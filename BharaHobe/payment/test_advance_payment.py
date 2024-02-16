from django.test import TestCase
from django.core.exceptions import ValidationError
from .forms import advancePaymentForm

class TestAdvancePaymentForm(TestCase):
    """
    Test cases for the Advance Payment Form.

    Attributes:
        valid_credit_card_data (advancePaymentFormData): Valid form data for advance payment.
        invalid_credit_card_data (advancePaymentFormData): Invalid form data for advance payment.

    Methods:
        setUp: Sets up common data for the test cases.
        test_valid_credit_card: Test form validation for a valid credit card.
        test_invalid_credit_card: Test form validation for an invalid credit card.
        test_duplicate_payment: Test for attempting to make a duplicate payment.
    """
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

    def test_valid_credit_card(self):
        """Test form validation for a valid credit card."""
        
        form = advancePaymentForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['f_card_token'], 'mock_card_token')

    def test_invalid_credit_card(self):
        """Test form validation for an invalid credit card."""
        with self.assertRaises(ValidationError) as context:
            advancePaymentForm(data=self.invalid_credit_card_data).full_clean()

        expected_error_message = 'Invalid credit card number'
        self.assertEqual(str(context.exception), expected_error_message)

    def test_duplicate_payment(self):
        """Test for attempting to make a duplicate payment."""
        response = self.client.post('/advance_payment_form/1', data=self.valid_credit_card_data)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    import unittest
    unittest.main()
