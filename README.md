
# Inventory Data Processor

A command-line Python tool that:
- Reads inventory data from inventory.csv
- Validates rows using Pydantic
- Logs invalid rows to errors.log
- Generates a low_stock_report.txt for products below quantity 10

## Requirements
pip install pydantic

## Run
python3 processor.py

## File Outputs
- errors.log → Contains validation problems
- low_stock_report.txt → All products with quantity < 10
