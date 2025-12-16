from datetime import date

from core import Inventory
from models import BookProduct, ElectronicProduct, FoodProduct

milk = FoodProduct("F001", "Milk", 5, 40.0, date(2025, 1, 15))
laptop = ElectronicProduct("E100", "Laptop", 2, 60000.0, 24)
clean_code = BookProduct("B777", "Clean Code", 10, 550.0, "Robert C. Martin", 2008)

inventory = Inventory()
inventory.add_product(milk)
inventory.add_product(laptop)
inventory.add_product(clean_code)

print(milk)
print(laptop)
print(clean_code)
print()

print("Laptop total value:", laptop.get_total_value())
print("Clean Code low stock?:", clean_code.is_low_stock())
print()

print(inventory)
print("Low stock products:", [str(p) for p in inventory.low_stock_products()])
inventory.generate_report()
