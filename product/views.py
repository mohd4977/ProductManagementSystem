from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from authenticator.permissions import IsInventoryManager

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsInventoryManager]
