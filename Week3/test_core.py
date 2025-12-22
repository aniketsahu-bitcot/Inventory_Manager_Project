
# 1. SUCCESSFUL FLOW TESTS 

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

def test_low_stock_products(inventory_with_multiple_products, laptop_product, low_stock_product):
    
    inventory = inventory_with_multiple_products

    
    low_stock_items = inventory.low_stock_products()

    
    assert len(low_stock_items) == 2
    assert laptop_product in low_stock_items
    assert low_stock_product in low_stock_items

def test_inventory_str_representation(inventory_with_multiple_products):
    
    inventory = inventory_with_multiple_products

    
    result = str(inventory)

    
    assert result.startswith("3 items")


# 2. BOUNDARY TESTS 

def test_inventory_value_empty(empty_inventory):
    # Arrange
    inventory = empty_inventory

    # Act
    value = inventory.get_inventory_value()

    # Assert
    assert value == 0.0

def test_empty_low_stock(empty_inventory):
    
    inventory = empty_inventory

   
    low_stock = inventory.low_stock_products(threshold=5)

    
    assert len(low_stock) == 0


# 3. FAILURE MODE TESTS 

def test_remove_nonexistent_product(empty_inventory):
    # Arrange
    inventory = empty_inventory

    # Act
    inventory.remove_product("NONEXISTENT")

    # Assert
    assert len(inventory.products) == 0

def test_add_duplicate_overwrites(inventory_with_one_product, laptop_product):
   
    original_name = laptop_product.name
    original_qty = laptop_product.quantity
    laptop_product.name = "Duplicate Laptop"
    laptop_product.quantity = 3

 
    inventory_with_one_product.add_product(laptop_product)
    result = inventory_with_one_product.get_product("P001")

   
    assert result.name == "Duplicate Laptop"
    assert result.quantity == 3

  
    laptop_product.name = original_name
    laptop_product.quantity = original_qty


# 4. EXACT LIMIT TESTS 

def test_single_product_exact_limit(inventory_with_one_product):
    # Arrange
    inventory = inventory_with_one_product  

    # Act
    product_count = len(inventory.products)
    total_value = inventory.get_inventory_value()

    # Assert
    assert product_count == 1
    assert total_value == 250000.0  

def test_low_stock_exact_threshold(inventory_with_multiple_products, laptop_product, low_stock_product):
    
    inventory = inventory_with_multiple_products

    
    low_stock_items = inventory.low_stock_products(threshold=6)

    
    assert len(low_stock_items) == 2
    assert laptop_product in low_stock_items      
    assert low_stock_product in low_stock_items  

