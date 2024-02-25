# """
# Unit tests for the PaymentModel class in models.py
# """

# import pytest
# from ..models import PaymentModel

# @pytest.mark.django_db
# def test_payment_creation():
#     """
#     Test case to verify the successful creation of a payment instance.
#     """
#     payment = PaymentModel.objects.create(m_order_id='123', m_amount=50.00, m_payment_method='credit_card')
#     assert payment.m_order_id == '123'
#     assert payment.m_amount == 50.00

# @pytest.mark.django_db
# def test_payment_success():
#     """
#     Test case to verify that a payment instance can be marked as successful.
#     """
#     payment = PaymentModel.objects.create(m_order_id='123', m_amount=50.00, m_payment_method='credit_card', m_isSuccess=True)
#     assert payment.m_isSuccess == True
