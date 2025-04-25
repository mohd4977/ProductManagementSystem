from celery import chain, shared_task
from django.core.mail import send_mail
from decimal import Decimal
import csv
from io import StringIO

from .models import Product

@shared_task
def import_csv_task(file_path):
    
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    'sku': row['sku'],
                    'inventory_quantity': int(row['inventory_quantity'])
                })
    except FileNotFoundError:
        raise Exception(f"CSV file not found at: {file_path}")
    return data

@shared_task
def validate_and_update_inventory(data):

    updated = []

    for item in data:
        try:
            product = Product.objects.get(sku=item['sku'])
            old_qty = product.inventory_quantity
            product.inventory_quantity = item['inventory_quantity']
            product.save()
            updated.append((item['sku'], old_qty, item['inventory_quantity']))
        except Product.DoesNotExist:
            continue
    return updated

@shared_task
def send_inventory_report(updates):
    report_lines = [
        f"SKU: {sku}, Old: {old}, New: {new}" for sku, old, new in updates
    ]
    report = "\n".join(report_lines)
    
    send_mail(
        subject='Nightly Inventory Update Report',
        message=report or "No updates performed.",
        from_email='noreply@example.com',
        recipient_list=['admin@example.com'],
    )
    return "Report emailed."

def run_nightly_inventory_chain(csv_content):
    chain(
        import_csv_task.s(csv_content),
        validate_and_update_inventory.s(),
        send_inventory_report.s()
    ).apply_async()
    return "Report emailed."