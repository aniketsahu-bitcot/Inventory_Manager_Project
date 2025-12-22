# Inventory Data Processor

A professional command-line Python tool for inventory management.

## Features

- Learned to use OOP to manage complexity by combining data (attributes) and behavior (methods) into classes.

- Refactored the procedural inventory script into Product and Inventory classes following the Single Responsibility Principle (SRP).

- Applied inheritance and the Open/Closed Principle (OCP) to create specialized product types like FoodProduct.

- Structured the project as a Python package with proper modules, type hints, docstrings, and code quality tools (ruff, black).

- Learned about TDD's Testing Pyramid prioritizes unit tests via Red-Green-Refactor; Pytest fixtures enable AAA for reusable, clean specs.

- Written test functions, run pytest; added fixtures with AAA pattern.

## Learning Journey
- [Week 1 to 3 Overview](Docs/INDEX.md)
- [Architecture](Docs/ARCHITECTURE.md)
- [Setup & Installation](Docs/SETUP.md)
- [Testing Guide](Docs/TESTING.md)


## Tech Stack
- Language: Python
- Testing: Pytest
- Linting: Ruff
- Formatting: Black

## Project Folder Structure:
```
├── Docs/
├── README.md
├── requirements.txt
├── Week1/
└── Week2/
└── Week3/
```

---

## Installation

1. Clone the repository:

```
git clone <repository-url>
```
2. Navigate to the Project Directory

```
cd project_name
```

3. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

4. Install dependencies:
```
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```
pytest
```

## Code Quality

Run linting:
```
ruff check .
```

Format code:
```
black .
```