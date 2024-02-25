# import pytest
# from django.urls import reverse
# from django.test import Client
# from django.http import HttpResponseBadRequest
# from ..models import OrderModel, PaymentModel

# @pytest.mark.django_db
# def test_display_advance_payment_form():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
#     response = client.get(reverse('advance_payment_view', args=[order.id]))
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_successful_advance_payment():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
#     response = client.post(reverse('advance_payment_view', args=[order.id]), data={
#         'f_payment_method': 'credit_card',
#         'f_credit_card_number': '1234567812345670',  # Valid mock credit card number
#         'f_amount': 100.00,
#         'f_notes': 'Some notes'
#     })
#     assert response.status_code == 200
#     assert 'payment_success' in response.templates[0].name

# @pytest.mark.django_db
# def test_duplicate_advance_payment():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
#     PaymentModel.objects.create(m_order_id=order.m_order_id, m_amount=50.00, m_payment_method='credit_card', m_isSuccess=True)
    
#     response = client.post(reverse('advance_payment_view', args=[order.id]), data={
#         'f_payment_method': 'credit_card',
#         'f_credit_card_number': '1234567812345670',  # Valid mock credit card number
#         'f_amount': 50.00,
#         'f_notes': 'Some notes'
#     })
#     assert response.status_code == 400
#     assert isinstance(response, HttpResponseBadRequest)
#     assert 'Payment for this order has already been made.' in response.content.decode()

# @pytest.mark.django_db
# def test_incorrect_amount_advance_payment():
#     client = Client()
#     order = OrderModel.objects.create(m_order_id='123', m_items='Item1, Item2', m_total_amount=100.00)
    
#     response = client.post(reverse('advance_payment_view', args=[order.id]), data={
#         'f_payment_method': 'credit_card',
#         'f_credit_card_number': '1234567812345670',  # Valid mock credit card number
#         'f_amount': 80.00,  # Incorrect amount
#         'f_notes': 'Some notes'
#     })
#     assert response.status_code == 400
#     assert isinstance(response, HttpResponseBadRequest)
#     assert 'Please pay the exact amount.' in response.content.decode()
