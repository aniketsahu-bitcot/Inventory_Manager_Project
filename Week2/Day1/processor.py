from pydantic import BaseModel, Field


class Product(BaseModel):
    product_id: str
    name: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0.0)

    def get_total_value(self) -> float:
        """Return total value of this product's stock."""
        return self.quantity * self.price

    def is_low_stock(self, threshold: int = 10) -> bool:
        """Check if product is low stock based on threshold."""
        return self.quantity < threshold

    def restock(self, amount: int):
        """Increase the quantity."""
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")
        self.quantity += amount

    def purchase(self, amount: int):
        """Reduce quantity after purchase."""
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")
        if amount > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= amount

    def __str__(self):
        return (
            f"{self.name} (ID: {self.product_id}) - "
            f"Qty: {self.quantity}, Price: {self.price}"
        )


p = Product(product_id="P1", name="Mouse", quantity=10, price=250.0)

print(p)

print("Total value:", p.get_total_value())


print("Is low stock:", p.is_low_stock())


p.restock(5)
print("After restock:", p)


p.purchase(3)
print("After purchase:", p)
