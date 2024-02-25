import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product, Cart

@pytest.fixture
def api_client():
    """
    Fixture to create an instance of Django's APIClient for making API requests.
    """
    return APIClient()

@pytest.fixture
def test_user():
    """
    Fixture to create a test user.
    """
    return User.objects.create_user(username='test_user', password='password')

@pytest.fixture
def test_product():
    """
    Fixture to create a test product.
    """
    return Product.objects.create(name='Test Product', price=100)

@pytest.mark.django_db
def test_add_to_cart(api_client, test_user, test_product):
    """
    Test function to verify adding a product to the cart.
    """
    # Login the test user
    api_client.force_authenticate(user=test_user)

    # Send a POST request to add the product to the cart
    response = api_client.post(reverse('add_to_cart'), {'product_id': test_product.id})

    # Check if the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Check if the product was added to the cart
    cart = Cart.objects.get(user=test_user)
    assert cart.cart_items.filter(product=test_product).exists()

    # Optionally, check the response data for additional details
    assert response.data['message'] == 'Product added to cart successfully'
