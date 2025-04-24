from django.contrib import admin
from .models import Product
from django.utils.html import format_html
from django.utils.timezone import localtime
from decimal import Decimal

@admin.action(description='Increase price by 10 percent')
def increase_price_10(modeladmin, request, queryset):
    for product in queryset:
        product.price *= Decimal('1.10')
        product.save()

@admin.action(description='Decrease price by 20 percent')
def decrease_price_20(modeladmin, request, queryset):
    for product in queryset:
        product.price *= Decimal('0.80')
        product.save()

@admin.action(description='Set price to $9.99')
def set_price_999(modeladmin, request, queryset):
    queryset.update(price=Decimal('9.99'))

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'inventory_quantity', 'formatted_last_updated')
    list_filter = ('last_updated',)  # basic filtering by date
    search_fields = ('name', 'sku')
    ordering = ('-last_updated',)
    actions = [increase_price_10, decrease_price_20, set_price_999]
    
    def formatted_last_updated(self, obj):
        return localtime(obj.last_updated).strftime('%Y-%m-%d %H:%M:%S')
    formatted_last_updated.short_description = 'Last Updated'

# Register your models here.
