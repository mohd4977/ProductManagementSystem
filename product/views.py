from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from authenticator.permissions import IsInventoryManager
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from django.utils.decorators import method_decorator
import json

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsInventoryManager]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ProductFilter
    filterset_fields = ['name','sku']
    ordering_fields = ['id']
    ordering = ['id']
    search_fields = ['name', 'sku']


class ShopifyInventoryWebhook(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            payload = json.loads(request.body)
            sku = payload.get('sku')
            new_quantity = payload.get('inventory_quantity')

            if not sku or new_quantity is None:
                return Response({"error": "Missing sku or inventory_quantity"}, status=400)

            try:
                product = Product.objects.get(sku=sku)
                product.inventory_quantity = new_quantity
                product.save()
                return Response({"message": f"Inventory updated for {sku}"}, status=200)
            except Product.DoesNotExist:
                return Response({"error": f"Product with sku '{sku}' not found"}, status=404)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=400)
