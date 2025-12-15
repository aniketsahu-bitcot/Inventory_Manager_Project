from pydantic import BaseModel, Field
import csv


class Product(BaseModel):
    product_id: str
    name: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0.0)

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Qty: {self.quantity}, Price: {self.price}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product | None:
        return self.products.get(product_id)

    def load_from_csv(self, file_path: str):
        try:
            with open(file_path, "r") as file:  # Fixed: Use file_path parameter
                reader = csv.DictReader(file)
                for row in reader:
                    # Handle both "name" and "product_name" for flexibility
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

    def generate_report(self):
        print("\nInventory Report:")
        total_value = 0
        for product in self.products.values():
            value = product.quantity * product.price
            print(f"{product.name} | Qty: {product.quantity} | Value: {value}")
            total_value += value
        print("Total Inventory Value:", total_value)



inventory = Inventory()


p1 = Product(product_id="P1", name="Mouse", quantity=10, price=250)
p2 = Product(product_id="P2", name="Keyboard", quantity=5, price=500)

inventory.add_product(p1)
inventory.add_product(p2)

inventory.load_from_csv("inventory.csv")

inventory.generate_report()
