# Inventory Manager Project:

## 1. Introduction
Command-line Python tool that reads inventory.csv, validates products using Pydantic, logs errors, and generates low-stock reports. It comprises an OOP package adhering to SRP, OCP, and best practices. Pytest supports reusability with simple test execution and reusable fixtures, using the Arrange-Act-Assert pattern to keep tests clean and maintainable.

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

### Week 3: TDD with Pytest
- **Introduction of TDD using Pytest**: TDD with Pytest treats tests as specifications, emphasizing unit tests via the Testing Pyramid and the Red-Green-Refactor cycle.
- **Fixtures**: Pytest supports reusability with simple test execution and reusable fixtures, using the Arrange-Act-Assert pattern to keep tests clean and maintainable

## 3. Project Goals

- Implement core functionality to read inventory.csv, validate rows with Pydantic, log invalid entries to errors.log, and create low_stock_report.txt for items under 10 units (Week 1 tasks).

- Develop Product class with data bundling and methods like get_total_value(); apply SRP via separate Product and Inventory classes; use inheritance for OCP with subclasses like FoodProduct and ElectronicProduct; ensure code quality with Ruff, Black, docstrings, type hints, and pyproject.toml packaging (Week 2 tasks).

- Treat tests as specifications using the Testing Pyramid and Red-Green-Refactor cycle; leverage fixtures for reusable, clean tests following Arrange-Act-Assert (Week 3 tasks).