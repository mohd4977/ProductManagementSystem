import pytest
from rest_framework.test import APIClient
from product.models import Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def product(db):
    return Product.objects.create(name="Hooked Product", sku="WEB123", price=20.0, inventory_quantity=5)

def test_webhook_inventory_update(api_client, product):
    data = {
        "sku": "WEB123",
        "inventory_quantity": 99
    }
    response = api_client.post("/api/webhooks/shopify/inventory/", data, format='json')
    assert response.status_code == 200

    product.refresh_from_db()
    assert product.inventory_quantity == 99