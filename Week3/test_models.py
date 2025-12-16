


def test_product_initialization(laptop_product):
    # Arrange
    product = laptop_product

    # Act
    product_id = product.product_id
    name = product.name
    quantity = product.quantity
    price = product.price

    # Assert
    assert product_id == "P001"
    assert name == "Laptop"
    assert quantity == 5
    assert price == 50000.0


def test_get_total_value(mouse_product):

    product = mouse_product

    total_value = product.get_total_value()

    assert total_value == 5000.0


def test_is_low_stock_true(low_stock_product):

    product = low_stock_product

    result = product.is_low_stock()

    assert result is True


def test_is_low_stock_false(monitor_product):

    product = monitor_product

    result = product.is_low_stock()

    assert result is False


def test_is_low_stock_with_custom_threshold(headphones_product):

    product = headphones_product

    result_high = product.is_low_stock(threshold=10)
    result_low = product.is_low_stock(threshold=5)

    assert result_high is True
    assert result_low is False


def test_str_representation(tablet_product):

    product = tablet_product

    result = str(product)

    assert result == "Tablet (ID: P006)"
