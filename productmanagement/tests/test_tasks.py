from unittest.mock import patch
from product.tasks import import_csv_task, validate_and_update_inventory, send_inventory_report
from product.models import Product

def test_import_csv_from_file(tmp_path):
    # Create mock CSV
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("sku,inventory_quantity\nSKU123,50")

    result = import_csv_task(str(csv_file))
    print(result)
    assert result == [{'sku': 'SKU123', 'inventory_quantity': 50}]

def test_validate_and_update_inventory(db):
    product = Product.objects.create(name="X", sku="SKU123", price=10, inventory_quantity=5)
    data = [{'sku': 'SKU123', 'inventory_quantity': 100}]
    updates = validate_and_update_inventory(data)
    product.refresh_from_db()
    assert product.inventory_quantity == 100
    assert updates == [('SKU123', 5, 100)]

@patch("product.tasks.send_mail")
def test_send_inventory_report(mock_send_mail):
    updates = [('SKU123', 10, 50)]
    result = send_inventory_report(updates)
    assert mock_send_mail.called
    assert result == "Report emailed."