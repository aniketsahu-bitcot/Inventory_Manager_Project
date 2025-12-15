

class Product:
    """Base Product class with common attributes.

    Attributes:
        product_id (str): Unique ID of the product.
        name (str): Name of the product.
        quantity (int): Available stock count.
        price (float): Price per unit.
    """

    def __init__(self, product_id: str, name: str, quantity: int, price: float) -> None:
        """Initialize a Product instance.

        Args:
            product_id (str): Unique product ID.
            name (str): Name of the product.
            quantity (int): Quantity in stock.
            price (float): Price per unit.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_total_value(self) -> float:
        """Calculate the total value of the product stock.

        Returns:
            float: Total stock value (quantity * price).
        """
        return self.quantity * self.price

    def is_low_stock(self, threshold: int = 10) -> bool:
        """Check if the product is low in stock.

        Args:
            threshold (int, optional): Stock threshold. Defaults to 10.

        Returns:
            bool: True if quantity is below the threshold, otherwise False.
        """
        return self.quantity < threshold

    def __str__(self) -> str:
        """String representation of the product.

        Returns:
            str: Human-readable product description.
        """
        return f"{self.name} (ID: {self.product_id})"