# Inventory Manager Project Weekly Overview:

## 1. Introduction
Command-line Python tool that reads inventory.csv, validates products using Pydantic, logs errors, and generates low-stock reports. It comprises OOP package with SRP, OCP, and best practices.

## 2. Features

### Week 1: Initial Functionality
- Reads inventory data from `inventory.csv`
- Validates rows using Pydantic
- Logs invalid rows to `errors.log`
- Generates `low_stock_report.txt` for products with quantity < 10

### Week 2: OOP Refactoring & Enhancements
- **Object-Oriented Design**: `Product` class bundles data (`price`, `quantity`) + methods (`get_total_value()`)
- **Single Responsibility Principle (SRP)**: `Product` (individual items) + `Inventory` (collection management)
- **Inheritance & OCP**: Base `Product` with subclasses (`FoodProduct`, `ElectronicProduct`) - extensible without modification
- **Professional code quality**: Ruff linter, Black formatter, Google-style docstrings, full type hints
- **Package Structure**: Proper Python package with `pyproject.toml`

