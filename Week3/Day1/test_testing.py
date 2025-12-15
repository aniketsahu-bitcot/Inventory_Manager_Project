from models import Product


def test_product_initialization():
    product = Product("P001", "Laptop", 5, 50000.0)

    assert product.product_id == "P001"
    assert product.name == "Laptop"
    assert product.quantity == 5
    assert product.price == 50000.0


def test_get_total_value():
    product = Product("P002", "Mouse", 10, 500.0)

    assert product.get_total_value() == 5000.0


def test_is_low_stock_true():
    product = Product("P003", "Keyboard", 3, 1500.0)

    assert product.is_low_stock() is True


def test_is_low_stock_false():
    product = Product("P004", "Monitor", 20, 12000.0)

    assert product.is_low_stock() is False


def test_is_low_stock_with_custom_threshold():
    product = Product("P005", "Headphones", 8, 2000.0)

    assert product.is_low_stock(threshold=10) is True
    assert product.is_low_stock(threshold=5) is False


def test_str_representation():
    product = Product("P006", "Tablet", 7, 25000.0)

    assert str(product) == "Tablet (ID: P006)"
