import pytest
from Week2.Day5.inventory_manager.models import Product
from Week2.Day5.inventory_manager.core import Inventory


@pytest.fixture
def laptop_product():
    return Product("P001", "Laptop", 5, 50000.0)


@pytest.fixture
def mouse_product():
    return Product("P002", "Mouse", 10, 500.0)


@pytest.fixture
def low_stock_product():
    return Product("P003", "Keyboard", 3, 1500.0)


@pytest.fixture
def monitor_product():
    return Product("P004", "Monitor", 20, 12000.0)


@pytest.fixture
def headphones_product():
    return Product("P005", "Headphones", 8, 2000.0)


@pytest.fixture
def tablet_product():
    return Product("P006", "Tablet", 7, 25000.0)


@pytest.fixture
def empty_inventory():
    return Inventory()


@pytest.fixture
def inventory_with_one_product(laptop_product):
    inventory = Inventory()
    inventory.add_product(laptop_product)
    return inventory


@pytest.fixture
def inventory_with_multiple_products(laptop_product, mouse_product, low_stock_product):
    inventory = Inventory()
    inventory.add_product(laptop_product)
    inventory.add_product(mouse_product)
    inventory.add_product(low_stock_product)
    return inventory
