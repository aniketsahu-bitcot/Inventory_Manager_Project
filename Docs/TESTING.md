# Testing & Test Driven Development Practices Guide

## 1. Introduction
This document explains the testing strategy used in this project, the tools involved, and how to run and write tests effectively.

---
## 2. Testing Philosophy
- The project follows **Test-Driven Development (TDD)** to ensure correctness and clean design.
- Testing is guided by the **Testing Pyramid**, prioritizing **unit tests** over integration and end-to-end tests.
- Development follows the **Red–Green–Refactor** cycle:
  - **Red**: Write a failing test
  - **Green**: Write minimal code to pass the test
  - **Refactor**: Improve code while keeping tests green
- **Pytest** is used as the primary testing framework.
- Test functions are written and executed using `pytest` to validate behavior early.
- **Pytest fixtures** provide reusable and pre-configured test data.
- The **Arrange–Act–Assert (AAA)** pattern is followed in every test to improve clarity and consistency.

---

## 3. Learnings:
- Red Green Refactor Cycle
- Importance of Fixtures for resusability

---

## 4. Project Test Structure
```
Week3
├── conftest.py
├── __init__.py
├── __pycache__
├── test_core.py
└── test_models.py
```
---
## 5. Key Principles
- TDD with Pytest treats tests as specifications, emphasizing unit tests via the Testing Pyramid and the Red-Green-Refactor cycle.
- Pytest supports reusability with simple test execution and reusable fixtures, using the Arrange-Act-Assert pattern to keep tests clean and maintainable

--- 

## 6. Requirements
```
pytest>=8.0.0
ruff>=0.5.0
black>=24.0.0

```
--- 

## 7. Tools Used
- **pytest** – Test framework
- **fixtures** – Test setup and reuse
- **ruff** – Code quality and linting
- **black**  – For code formatting

---
## 8. Running Tests

Run all tests:

```
pytest
```

## 9. Best Practices

- Write tests before code (TDD)
- Keep tests small and focused
- Avoid testing implementation details
- Prefer unit tests over integration tests

## 10. Common Mistakes

- Writing overly complex tests
- Sharing state between tests
- Skipping edge cases
- Ignoring failing tests12. Conclusion

## 11. Conclusion
Testing ensures code correctness, improves design, and provides confidence during refactoring and feature development.

