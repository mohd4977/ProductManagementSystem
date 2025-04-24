import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    inventory_quantity__gt = django_filters.NumberFilter(field_name='inventory_quantity', lookup_expr='gt')
    inventory_quantity__lt = django_filters.NumberFilter(field_name='inventory_quantity', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['inventory_quantity__gt', 'inventory_quantity__lt']