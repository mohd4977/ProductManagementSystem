import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from product.models import Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def inventory_user(db):
    user = User.objects.create_user(username="testuser", password="pass")
    group = Group.objects.create(name="inventory_managers")
    user.groups.add(group)
    return user

@pytest.fixture
def product(db):
    return Product.objects.create(name="Test Product", sku="SKU123", price=10.0, inventory_quantity=5)

def test_product_list_auth(api_client, inventory_user):
    api_client.force_authenticate(user=inventory_user)
    response = api_client.get('/api/products/')
    assert response.status_code == 200

def test_product_create(api_client, inventory_user):
    api_client.force_authenticate(user=inventory_user)
    data = {
        "name": "New Product",
        "sku": "NEWSKU123",
        "price": "15.50",
        "inventory_quantity": 10
    }
    response = api_client.post('/api/products/', data, format='json')
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
    assert response.status_code == 201