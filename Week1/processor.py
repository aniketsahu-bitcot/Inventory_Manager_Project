"""
Simple Inventory Data Processor

This program:
1. Reads inventory.csv using the csv module
2. Validates each row using a simple Pydantic model
3. Logs mistakes in errors.log
4. Creates a low_stock_report.txt for products with quantity < 10
"""

import csv
from pydantic import BaseModel, ValidationError
from typing import List


class Product(BaseModel):
    """Simple Product Model"""

    product_id: int
    product_name: str
    quantity: int
    price: float


def read_inventory() -> List[Product]:
    """Reads the CSV file and returns a list of valid Product objects"""

    products = []

    # open logs file in append mode
    error_file = open("errors.log", "a")

    with open("inventory.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                # Create Product object (Pydantic auto-validates types)
                product = Product(
                    product_id=int(row["product_id"]),
                    product_name=row["product_name"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"]),
                )
                products.append(product)
            except (ValidationError, ValueError) as e:
                error_file.write(f"Invalid row: {row} -> {e}\n")

    error_file.close()
    return products


def create_low_stock_report(products: List[Product]) -> None:
    """Writes products with quantity < 10 into a text file"""

    with open("low_stock_report.txt", "w") as file:
        file.write("Low Stock Products (Quantity < 10)\n")
        file.write("---------------------------------\n")

        for p in products:
            if p.quantity < 10:
                file.write(f"{p.product_id} - {p.product_name} - Qty: {p.quantity}\n")


products = read_inventory()
create_low_stock_report(products)
print("Done! Check low_stock_report.txt and errors.log.")
