import csv
from models import Product  # Import from models.py


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
        return sum(
            p.get_total_value() for p in self.products.values()
        )  # Using total_value from models.py

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
            value = product.get_total_value()  # Using total_value from models.py
            print(f"{product.name} | Qty: {product.quantity} | Value: {value}")
            total_value += value
        print("Total Inventory Value:", total_value)

    def __str__(self):
        return f"Inventory with {len(self.products)} products, total value: ${self.total_inventory_value():,.2f}"
