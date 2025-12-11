from models import FoodProduct
from models import ElectronicProduct
from models import BookProduct
from datetime import date


p1 = FoodProduct("F001", "Milk", 5, 40.0, date(2025, 1, 15))
p2 = ElectronicProduct("E100", "Laptop", 2, 60000.0, 24)
p3 = BookProduct("B777", "Clean Code", 10, 550.0, "Robert C. Martin", 2008)

print(p1)
print(p2)
print(p3)

print("Laptop total value:", p2.total_value())
print("Clean Code low stock?:", p3.is_low_stock())
