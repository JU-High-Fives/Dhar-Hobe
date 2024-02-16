from django.test import TestCase
from .models import OrderModel
import unittest

class ShowOrdersViewTests(TestCase):
    """
    Test cases for the Show Orders View.

    Attributes:
        order (OrderModel): A dummy instance of OrderModel for testing.

    Methods:
        setUp: Creates a dummy OrderModel instance for testing.
        test_order_str_representation: Checks the correctness of the order ID representation.
        test_order_unique_constraint: Ensures that an order ID is unique.
        test_order_notes_blank_or_null: Checks that the note field can be empty for order creation.
    """
    def setUp(self):
        """Create a dummy OrderModel instance for testing."""
        self.order = OrderModel.objects.create(
            m_order_id='123456',
            m_items='Item1, Item2, Item3',
            m_total_amount=150.50,
            m_notes='Some notes for the order'
        )
        self.duplicate_order = OrderModel.objects.create(
            m_order_id='123456', 
            m_items='Another Item',
            m_total_amount=30.75,
        )
        self.order_with_blank_notes = OrderModel.objects.create(
            m_order_id='789012',
            m_items='Item4, Item5',
            m_total_amount=75.25,
            m_notes='',
        )
        self.order_with_null_notes = OrderModel.objects.create(
            m_order_id='345678',
            m_items='Item6, Item7',
            m_total_amount=120.00,
            m_notes=None,
        )

    def test_order_str_representation(self):
        """Check whether the order ID representation is correct."""
        self.assertEqual(str(self.order), "Order #123456")

    def test_order_unique_constraint(self):
        """Ensure that an order ID is unique."""
        
        with self.assertRaises(Exception):
            self.duplicate_order.save()

    def test_order_notes_blank_or_null(self):
        """Check that the note field can be empty for order creation."""
        
        self.order_with_blank_notes.save()
        self.order_with_null_notes.save()

        self.assertEqual(self.order_with_blank_notes.m_notes, '')
        self.assertIsNone(self.order_with_null_notes.m_notes)


if __name__ == '__main__':
    unittest.main()
