from pydantic import BaseModel, Field
import csv


# PRODUCT (Only holds data)
class Product(BaseModel):
    product_id: str
    name: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0.0)

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Qty: {self.quantity}, Price: {self.price}"


# INVENTORY
class Inventory:
    def __init__(self):
        self.products = {}

    # Add product to inventory
    def add_product(self, product: Product):
        self.products[product.product_id] = product

    # Get product by ID
    def get_product(self, product_id: str) -> Product:
        return self.products.get(product_id)

    # Load products from CSV
    # CSV Format: product_id,name,quantity,price
    def load_from_csv(self, file_path: str):
        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    product_id=row["product_id"],
                    name=row["product_name"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"]),
                )
                self.add_product(product)

    # Create a simple report
    def generate_report(self):
        print("\nInventory Report:")
        total_value = 0

        for product in self.products.values():
            value = product.quantity * product.price
            print(f"{product.name} | Qty: {product.quantity} | Value: {value}")
            total_value += value

        print("Total Inventory Value:", total_value)


# EXAMPLE
inventory = Inventory()

# Add manual products
p1 = Product(product_id="P1", name="Mouse", quantity=10, price=250)
p2 = Product(product_id="P2", name="Keyboard", quantity=5, price=500)

inventory.add_product(p1)
inventory.add_product(p2)

inventory.load_from_csv("inventory.csv")
# Generate report
inventory.generate_report()
