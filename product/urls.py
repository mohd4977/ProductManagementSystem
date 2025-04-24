from django.urls import path
from .views import ShopifyInventoryWebhook

urlpatterns = [
    path('webhooks/shopify/inventory/', ShopifyInventoryWebhook.as_view(), name='shopify-inventory-webhook'),
]