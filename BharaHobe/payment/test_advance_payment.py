from django.test import TestCase
from .forms import advancePaymentForm

class TestAdvancePaymentForm(TestCase):
    def setUp(self):
        """Set up common data for the test cases."""
        self.valid_credit_card_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '4111111111111111',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }
        self.invalid_credit_card_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': 'invalid_card_number',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

    def test_valid_credit_card(self):
        """Test form validation for a valid credit card."""
        form = advancePaymentForm(data=self.valid_credit_card_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['f_card_token'], 'mock_card_token')

    def test_invalid_credit_card(self):
        """Test form validation for an invalid credit card."""
        form = advancePaymentForm(data=self.invalid_credit_card_data)
        self.assertFalse(form.is_valid())
        self.assertIn('f_credit_card_number', form.errors)
        self.assertEqual(form.errors['f_credit_card_number'][0], 'Invalid credit card number')


if __name__ == '__main__':
    import unittest
    unittest.main()
