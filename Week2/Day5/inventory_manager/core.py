import csv

from .models import Product


class Inventory:
    """Manages collection of products following SRP.

    Uses a dictionary keyed by product_id for O(1) lookup performance.
    Supports CSV loading, reporting, and inventory analytics.
    """

    def __init__(self) -> None:
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product: Product) -> None:
        """Add or replace a product in the inventory.

        Args:
            product: The Product instance to add.
        """
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product | None:
        """Retrieve a product by its ID.

        Args:
            product_id: The unique identifier of the product.

        Returns:
            The Product instance if found, None otherwise.
        """
        return self.products.get(product_id)

    def remove_product(self, product_id: str) -> None:
        """Remove a product from inventory by ID.

        Args:
            product_id: The unique identifier of the product to remove.
        """
        self.products.pop(product_id, None)

    def get_inventory_value(self) -> float:
        """Calculate total monetary value of all products.

        Returns:
            Float representing total inventory value.
        """
        return sum(p.get_total_value() for p in self.products.values())

    def low_stock_products(self, threshold: int = 10) -> list[Product]:
        """Find products below specified stock threshold.

        Args:
            threshold: Minimum quantity threshold (default: 10).

        Returns:
            List of Product instances with low stock.
        """
        return [p for p in self.products.values() if p.is_low_stock(threshold)]

    def load_from_csv(self, file_path: str) -> None:
        """Load products from CSV file into inventory.

        Supports columns: product_id, name (or product_name), quantity, price.
        Handles missing files gracefully.

        Args:
            file_path: Path to the CSV file.
        """
        try:
            with open(file_path) as file:
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

    def generate_report(self) -> None:
        """Print formatted inventory report to console.

        Shows each product with quantity and value, plus grand total.
        """
        print("\nInventory Report:")
        total_value = 0
        for product in self.products.values():
            value = product.get_total_value()
            print(f"{product.name} | Qty: {product.quantity} | Value: {value}")
            total_value += value
        print("Total Inventory Value:", total_value)

    def __str__(self) -> str:
        """String representation for printing.

        Returns:
            Formatted string with product count and total value.
        """
        return f"{len(self.products)} items: ${self.get_inventory_value():,.2f}"
