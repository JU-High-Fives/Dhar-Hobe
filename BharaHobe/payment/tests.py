from django.test import TestCase
from django.urls import reverse
from .models import OrderModel

class ShowOrdersViewTests(TestCase):
    def setUp(self):
        self.order = OrderModel.objects.create(
            m_order_id='123456',
            m_items='Item1, Item2, Item3',
            m_total_amount=150.50,
            m_notes='Some notes for the order'
        )

    def test_order_str_representation(self):
        self.assertEqual(str(self.order), "Order #123456")

    def test_order_unique_constraint(self):
        duplicate_order = OrderModel(
            m_order_id='123456', 
            m_items='Another Item',
            m_total_amount=30.75,
        )
        with self.assertRaises(Exception):
            duplicate_order.save()

    def test_order_notes_blank_or_null(self):
        order_with_blank_notes = OrderModel(
            m_order_id='789012',
            m_items='Item4, Item5',
            m_total_amount=75.25,
            m_notes='',
        )
        order_with_null_notes = OrderModel(
            m_order_id='345678',
            m_items='Item6, Item7',
            m_total_amount=120.00,
            m_notes=None,
        )
        order_with_blank_notes.save()
        order_with_null_notes.save()

        self.assertEqual(order_with_blank_notes.m_notes, '')
        self.assertIsNone(order_with_null_notes.m_notes)
