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

    def __init__(
        self, product_id: str, name: str, quantity: int, price: float, expiry_date: date
    ):
        super().__init__(product_id, name, quantity, price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{super().__str__()} - Expires on: {self.expiry_date}"


class ElectronicProduct(Product):
    """Special product with warranty period (in months)."""

    def __init__(
        self,
        product_id: str,
        name: str,
        quantity: int,
        price: float,
        warranty_period: int,
    ):
        super().__init__(product_id, name, quantity, price)
        self.warranty_period = warranty_period

    def __str__(self):
        return f"{super().__str__()} - Warranty: {self.warranty_period} months"


class BookProduct(Product):
    """Special product with author name and publication year."""

    def __init__(
        self,
        product_id: str,
        name: str,
        quantity: int,
        price: float,
        author: str,
        publication_year: int,
    ):
        super().__init__(product_id, name, quantity, price)
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return (
            f"{super().__str__()} - Author: {self.author}, "
            f"Published: {self.publication_year}"
        )


p1 = FoodProduct("F001", "Milk", 5, 40.0, date(2025, 1, 15))
p2 = ElectronicProduct("E100", "Laptop", 2, 60000.0, 24)
p3 = BookProduct("B777", "Clean Code", 10, 550.0, "Robert C. Martin", 2008)

print(p1)
print(p2)
print(p3)

print("Laptop total value:", p2.total_value())
print("Clean Code low stock?:", p3.is_low_stock())
