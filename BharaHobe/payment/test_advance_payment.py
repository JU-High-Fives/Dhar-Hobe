from django.test import TestCase
from .forms import advancePaymentForm
import unittest

class TestAdvancePaymentForm(TestCase):
    def test_valid_credit_card(self):
        form_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': '4111111111111111',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

        form = advancePaymentForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['f_card_token'], 'mock_card_token')

    def test_invalid_credit_card(self):
        form_data = {
            'f_payment_method': 'credit_card',
            'f_credit_card_number': 'invalid_card_number',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

        form = advancePaymentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('f_credit_card_number', form.errors)

    def test_non_credit_card_payment(self):
        form_data = {
            'f_payment_method': 'paypal',
            'f_credit_card_number': '4111111111111111',
            'f_notes': 'Test notes',
            'f_amount': 100.00,
            'f_card_token': '',
        }

        form = advancePaymentForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['f_card_token'], '')

if __name__ == '__main__':
    unittest.main()