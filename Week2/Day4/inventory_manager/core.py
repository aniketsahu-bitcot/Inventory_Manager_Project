from models import Product
from models import FoodProduct
from models import ElectronicProduct
from datetime import date

p = Product("P001", "Pen", 20, 10.5)
print(p)
print("Total value:", p.total_value())
print("Low stock?:", p.is_low_stock())

print("\n=== Testing FoodProduct ===")
fp = FoodProduct(
        product_id="F001",
        name="Milk",
        quantity=5,
        price=30.0,
        expiry_date=date(2025, 1, 10)
    )
print(fp)
print("Total value:", fp.total_value())
print("Low stock?:", fp.is_low_stock())

print("\n=== Testing ElectronicProduct ===")
ep = ElectronicProduct(
        product_id="E001",
        name="Laptop",
        quantity=3,
        price=1500.0,
        warranty_period=24
    )
print(ep)
print("Total value:", ep.total_value())
print("Low stock?:", ep.is_low_stock())