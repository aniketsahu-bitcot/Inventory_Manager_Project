from datetime import date


class Product:
    """Base Product class with common attributes."""

    def __init__(self, product_id: str, name: str, quantity: int, price: float):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self) -> float:
        return self.quantity * self.price

    def is_low_stock(self, threshold: int = 10) -> bool:
        return self.quantity < threshold

    def __str__(self):
        return f"{self.name} (ID: {self.product_id})"


class FoodProduct(Product):
    """Special product with expiry date."""

    def __init__(self, product_id: str, name: str, quantity: int, price: float, expiry_date: date):
        super().__init__(product_id, name, quantity, price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{super().__str__()} - Expires on: {self.expiry_date}"


class ElectronicProduct(Product):
    """Special product with warranty period (in months)."""

    def __init__(self, product_id: str, name: str, quantity: int, price: float, warranty_period: int):
        super().__init__(product_id, name, quantity, price)
        self.warranty_period = warranty_period

    def __str__(self):
        return f"{super().__str__()} - Warranty: {self.warranty_period} months"



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
        price=55000.0,
        warranty_period=24
    )
print(ep)
print("Total value:", ep.total_value())
print("Low stock?:", ep.is_low_stock())

