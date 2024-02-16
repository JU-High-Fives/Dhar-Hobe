from django.test import TestCase
from django.http import HttpResponseBadRequest
from .forms import advancePaymentForm
from .views import advance_payment_view
from django.core.exceptions import ValidationError
from .models import OrderModel, PaymentModel


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
            advancePaymentForm(data=form).full_clean()

        expected_error_message = 'Invalid credit card number'
        self.assertEqual(str(context.exception), expected_error_message)

    def test_invalid_credit_card(self):
        """Test form validation for an invalid credit card."""
        with self.assertRaises(ValidationError) as context:
            advancePaymentForm(data=self.invalid_credit_card_data).full_clean()

        expected_error_message = 'Invalid credit card number'
        self.assertEqual(str(context.exception), expected_error_message)

    def test_duplicate_payment(self):
        """Test for attempting to make a duplicate payment."""
        order = OrderModel.objects.create(
            m_order_id='123',
            m_items='Test items',
            m_total_amount=200.00,
            m_notes='Test order notes'
        )

        PaymentModel.objects.create(
            m_order_id=order.m_order_id,
            m_amount=100.00,
            m_isSuccess=True,
            m_payment_method='credit_card',
            m_notes='Test payment notes',
            m_card_token='mock_card_token'
        )

        request = self.client.post('/advance_payment_form/<int:order_id>/', data=self.valid_credit_card_data)
        self.assertEqual(request.status_code, HttpResponseBadRequest.status_code)
