from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer
from authenticator.permissions import IsInventoryManager
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

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
