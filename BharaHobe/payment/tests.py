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

    
