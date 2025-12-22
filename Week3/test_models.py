from datetime import date

# 1. SUCCESSFUL FLOW TESTS

def test_product_successful_init(laptop_product):
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

def test_product_successful_value(mouse_product):
  
    product = mouse_product
   
    total_value = product.get_total_value()

    assert total_value == 5000.0

def test_food_product_successful_init(food_product):
  
    product = food_product
  
    product_id = product.product_id
    name = product.name
    expiry = product.expiry_date
    
    assert product_id == "F001"
    assert name == "Milk"
    assert expiry == date(2025, 12, 25)

def test_electronic_product_successful_init(electronic_product):
   
    product = electronic_product

    warranty = product.warranty_period
    str_repr = str(product)
  
    assert warranty == 24
    assert "Warranty: 24 months" in str_repr

def test_book_product_successful_init(book_product):
  
    product = book_product
  
    author = product.author
    year = product.publication_year
    str_repr = str(product)
  
    assert author == "John Doe"
    assert year == 2023
    assert "Author: John Doe" in str_repr

# 2. BOUNDARY TESTS

def test_zero_quantity_boundary(laptop_product):
    # Arrange
    laptop_product.quantity = 0
    
    # Act
    total_value = laptop_product.get_total_value()
    
    # Assert
    assert total_value == 0.0
    laptop_product.quantity = 5  

def test_zero_price_boundary(laptop_product):
    
    laptop_product.price = 0.0
    
    total_value = laptop_product.get_total_value()
    
    assert total_value == 0.0
    laptop_product.price = 50000.0  

def test_food_expiry_today_boundary(food_product):
    
    food_product.expiry_date = date.today()
    
    str_repr = str(food_product)
    
    assert "Expires on:" in str_repr
    food_product.expiry_date = date(2025, 12, 25)  

def test_electronic_warranty_zero_boundary(electronic_product):
    
    electronic_product.warranty_period = 0
    
    str_repr = str(electronic_product)  
    
    assert "Warranty: 0 months" in str_repr
    electronic_product.warranty_period = 24 

def test_book_current_year_boundary(book_product):
    
    book_product.publication_year = 2025
    
    str_repr = str(book_product)
    
    assert "Published: 2025" in str_repr
    book_product.publication_year = 2023  


# 3. FAILURE MODE TESTS

def test_negative_quantity_failure(laptop_product):
    # Arrange
    laptop_product.quantity = -5
    
    # Act
    is_low = laptop_product.is_low_stock()
    
    # Assert
    assert is_low is True
    laptop_product.quantity = 5  

def test_electronic_negative_warranty_failure(electronic_product):
    
    electronic_product.warranty_period = -12
    
    str_repr = str(electronic_product) 
    
    assert "Warranty: -12 months" in str_repr
    electronic_product.warranty_period = 24  

def test_book_negative_year_failure(book_product):
   
    book_product.publication_year = -100
    
    str_repr = str(book_product)
    
    assert "Published: -100" in str_repr
    book_product.publication_year = 2023  

# 4. EXACT LIMIT TESTS

def test_exact_threshold_not_low(monitor_product):
    # Arrange
    product = monitor_product
    
    # Act
    is_low = product.is_low_stock(20)  
    
    # Assert
    assert is_low is False

def test_low_stock_exact_limit(low_stock_product):
    
    product = low_stock_product
    
    is_low = product.is_low_stock(3)  
    
    assert is_low is False

def test_is_low_stock_below_threshold(low_stock_product):
    
    product = low_stock_product
    
    result = product.is_low_stock()  
    
    assert result is True

def test_is_low_stock_above_threshold(monitor_product):
    
    product = monitor_product
    
    result = product.is_low_stock()  
    
    assert result is False

# 5. STRING REPRESENTATION TESTS

def test_product_str_successful(tablet_product):
    # Arrange
    product = tablet_product
    
    # Act
    result = str(product)
    
    # Assert
    assert result == "Tablet (ID: P006)"

def test_food_str_successful(food_product):
   
    product = food_product
  
    result = str(product)
    
    assert "Expires on: 2025-12-25" in result

def test_electronic_str_successful(electronic_product):
    
    product = electronic_product
    
    result = str(product)
    
    assert "Warranty: 24 months" in result

def test_book_str_successful(book_product):
    
    product = book_product
   
    result = str(product) 
   
    assert "Author: John Doe" in result
