import pytest
from Week2.Day5.inventory_manager.models import Product, FoodProduct, ElectronicProduct, BookProduct
from Week2.Day5.inventory_manager.core import Inventory
from datetime import date

# === PRODUCT FIXTURES (BASE CLASS) ===
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

# === SUBCLASS PRODUCT FIXTURES ===
@pytest.fixture
def food_product():
    return FoodProduct("F001", "Milk", 10, 2.5, date(2025, 12, 25))

@pytest.fixture
def electronic_product():
    return ElectronicProduct("E001", "Phone", 5, 500.0, 24)

@pytest.fixture
def book_product():
    return BookProduct("B001", "Python Guide", 20, 25.0, "John Doe", 2023)

# === INVENTORY FIXTURES (depend on products above) ===
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

