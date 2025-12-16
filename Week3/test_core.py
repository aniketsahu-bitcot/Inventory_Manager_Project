


def test_inventory_initialization(empty_inventory):
    # Arrange
    inventory = empty_inventory

    # Act
    products_count = len(inventory.products)
    inventory_value = inventory.get_inventory_value()

    # Assert
    assert products_count == 0
    assert inventory_value == 0.0
    assert isinstance(inventory.products, dict)


def test_add_and_get_product(inventory_with_one_product, laptop_product):

    inventory = inventory_with_one_product

    product = inventory.get_product(laptop_product.product_id)

    assert product is not None
    assert product.name == "Laptop"


def test_remove_product(inventory_with_one_product, laptop_product):

    inventory = inventory_with_one_product

    inventory.remove_product(laptop_product.product_id)
    result = inventory.get_product(laptop_product.product_id)

    assert result is None


def test_get_inventory_value(inventory_with_multiple_products):

    inventory = inventory_with_multiple_products

    total_value = inventory.get_inventory_value()

    expected = (5 * 50000.0) + (10 * 500.0) + (3 * 1500.0)
    assert total_value == expected


def test_low_stock_products(
    inventory_with_multiple_products, laptop_product, low_stock_product
):

    inventory = inventory_with_multiple_products

    low_stock_items = inventory.low_stock_products()

    assert len(low_stock_items) == 2
    assert laptop_product in low_stock_items
    assert low_stock_product in low_stock_items


def test_inventory_str_representation(inventory_with_multiple_products):

    inventory = inventory_with_multiple_products

    result = str(inventory)

    assert result.startswith("3 items")
