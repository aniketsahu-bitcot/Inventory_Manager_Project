from datetime import date
import csv


class Product:
    """Base Product class with common attributes."""

    def __init__(self, product_id: str, name: str, quantity: int, price: float):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_total_value(self) -> float:
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


class Inventory:
    """Manages collection of products following SRP."""

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product | None:
        return self.products.get(product_id)

    def remove_product(self, product_id: str):
        self.products.pop(product_id, None)

    def total_inventory_value(self) -> float:
        return sum(p.get_total_value() for p in self.products.values())

    def low_stock_products(self, threshold: int = 10) -> list[Product]:
        return [p for p in self.products.values() if p.is_low_stock(threshold)]

    def load_from_csv(self, file_path: str):
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row.get("name") or row.get("product_name")
                    product = Product(
                        product_id=row["product_id"],
                        name=name,
                        quantity=int(row["quantity"]),
                        price=float(row["price"]),
                    )
                    self.add_product(product)
        except FileNotFoundError:
            print(f"File {file_path} not found. Skipping CSV load.")
        except Exception as e:
            print(f"Error loading CSV: {e}")

    def generate_report(self):
        print("\nInventory Report:")
        total_value = 0
        for product in self.products.values():
            value = product.get_total_value()
            print(f"{product.name} | Qty: {product.quantity} | Value: {value}")
            total_value += value
        print("Total Inventory Value:", total_value)

    def __str__(self):
        return f"Inventory with {len(self.products)} products, total value: ${self.total_inventory_value():,.2f}"


# Example usage

# Create products
p1 = FoodProduct("F001", "Milk", 5, 40.0, date(2025, 1, 15))
p2 = ElectronicProduct("E100", "Laptop", 2, 60000.0, 24)
p3 = BookProduct("B777", "Clean Code", 10, 550.0, "Robert C. Martin", 2008)

# Create inventory and add products
inventory = Inventory()
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

# Test functionality
print(p1)
print(p2)
print(p3)
print()

print("Laptop total value:", p2.get_total_value())
print("Clean Code low stock?:", p3.is_low_stock())
print()

print(inventory)
print("Low stock products:", [str(p) for p in inventory.low_stock_products()])
inventory.generate_report()
