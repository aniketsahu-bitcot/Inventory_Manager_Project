from datetime import date


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

    def total_value(self) -> float:
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


class FoodProduct(Product):
    """Product subclass representing food items with expiry dates.

    Attributes:
        expiry_date (date): Date when the product expires.
    """

    def __init__(
        self,
        product_id: str,
        name: str,
        quantity: int,
        price: float,
        expiry_date: date,
    ) -> None:
        """Initialize a FoodProduct instance."""
        super().__init__(product_id, name, quantity, price)
        self.expiry_date = expiry_date

    def __str__(self) -> str:
        """String representation of the food product."""
        return f"{super().__str__()} - Expires on: {self.expiry_date}"


class ElectronicProduct(Product):
    """Product subclass representing electronics with a warranty period.

    Attributes:
        warranty_period (int): Warranty duration in months.
    """

    def __init__(
        self,
        product_id: str,
        name: str,
        quantity: int,
        price: float,
        warranty_period: int,
    ) -> None:
        """Initialize an ElectronicProduct instance."""
        super().__init__(product_id, name, quantity, price)
        self.warranty_period = warranty_period

    def __str__(self) -> str:
        """String representation of the electronic product."""
        return f"{super().__str__()} - Warranty: {self.warranty_period} months"


class BookProduct(Product):
    """Product subclass representing books with author and publication year.

    Attributes:
        author (str): Author of the book.
        publication_year (int): Publication year.
    """

    def __init__(
        self,
        product_id: str,
        name: str,
        quantity: int,
        price: float,
        author: str,
        publication_year: int,
    ) -> None:
        """Initialize a BookProduct instance."""
        super().__init__(product_id, name, quantity, price)
        self.author = author
        self.publication_year = publication_year

    def __str__(self) -> str:
        """String representation of the book product."""
        return (
            f"{super().__str__()} - Author: {self.author}, "
            f"Published: {self.publication_year}"
        )
