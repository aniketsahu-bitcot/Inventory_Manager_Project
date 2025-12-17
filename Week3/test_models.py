


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

def test_zero_quantity_from_fixture(laptop_product):
    
    laptop_product.quantity = 0  
    total_value = laptop_product.get_total_value()
    laptop_product.quantity = 5 
   
    assert total_value == 0.0  

def test_zero_price_from_fixture(laptop_product):
   
    laptop_product.price = 0.0  
  
    total_value = laptop_product.get_total_value()
    laptop_product.price = 50000.0  
   
    assert total_value == 0.0  

def test_negative_quantity_low_stock(laptop_product):
    
    laptop_product.quantity = -5  
 
    is_low = laptop_product.is_low_stock()
    laptop_product.quantity = 5 

    assert is_low is True 

# Test: High stock boundary (qty >= threshold → NOT low)
def test_exact_threshold_not_low(monitor_product):

    is_low = monitor_product.is_low_stock(20)  
  
    assert is_low is False 

# Test: Low stock boundary (qty == threshold → ?)
def test_low_stock_exact_boundary(low_stock_product):

    is_low = low_stock_product.is_low_stock(3) 
  
    assert is_low is False  

def test_fixture_restoration(laptop_product):
  
    original_qty = laptop_product.quantity
    
    laptop_product.quantity = 999
    laptop_product.quantity = original_qty
   
    assert laptop_product.quantity == 5
