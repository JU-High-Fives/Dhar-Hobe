# import pytest
# from django.urls import reverse
# from django.test import Client
# from django.http import HttpResponseBadRequest
# from ..models import OrderModel

# @pytest.mark.django_db
# def test_display_monthly_payment_form():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
#     response = client.get(reverse('monthly_payment_view', args=[order.id]))
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_successful_monthly_payment():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
#     response = client.post(reverse('monthly_payment_view', args=[order.id]), data={
#         'f_payment_method': 'credit_card',
#         'f_credit_card_number': '1234567812345670',  # Valid mock credit card number
#         'f_amount': 20.00,
#         'f_notes': 'Some notes'
#     })
#     assert response.status_code == 200
#     assert 'payment_success' in response.templates[0].name
#     assert order.m_total_amount == 80.00  # Monthly payment deducted from the total amount

# @pytest.mark.django_db
# def test_incorrect_amount_monthly_payment():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
    
#     response = client.post(reverse('monthly_payment_view', args=[order.id]), data={
#         'f_payment_method': 'credit_card',
#         'f_credit_card_number': '1234567812345670',  # Valid mock credit card number
#         'f_amount': 25.00,  # Incorrect amount
#         'f_notes': 'Some notes'
#     })
#     assert response.status_code == 400
#     assert isinstance(response, HttpResponseBadRequest)
#     assert 'Please pay the exact amount.' in response.content.decode()
