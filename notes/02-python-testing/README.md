
# Python Testing and Automation

## 1. Introduction

Python can be used to automate repetitive software testing
activities and execute test cases efficiently.

Pytest is a Python testing framework used to write,
organize and execute automated tests.

## 2. Basic Python Concepts for Testing

### Functions

Functions allow reusable blocks of code.

```python
def add(a, b):
    return a + b
```

### Conditional Statements

Used to validate conditions and control program behaviour.

```python
def validate_login(username, password):
    if not username or not password:
        return False

    if username == "admin" and password == "12345":
        return True

    return False
```

### Assertions

Assertions verify whether an actual result matches
the expected result.

```python
assert add(10, 20) == 30
```

If the condition is false, Python raises an AssertionError.

## 3. Introduction to Pytest

Pytest is a testing framework that makes it easier
to write and execute Python test cases.

### Installation

```bash
pip install pytest
```

### Naming Conventions

- Test files should generally start with `test_`.
- Test functions should start with `test_`.

Example:

```python
def test_addition():
    assert 10 + 20 == 30
```

### Running Tests

Run all tests:

```bash
python -m pytest
```

Run a particular test file:

```bash
python -m pytest tests/test_login.py -v
```

Verbose execution:

```bash
python -m pytest -v
```

## 4. Parameterization

Parameterization allows the same test function
to execute with multiple sets of input values.

```python
import pytest

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "12345", True),
        ("admin", "wrong", False),
        ("", "12345", False),
        ("admin", "", False)
    ]
)
def test_login(username, password, expected):
    result = validate_login(username, password)
    assert result == expected
```

Benefits:
- Reduces duplicate test code.
- Covers multiple input combinations.
- Improves test maintainability.

## 5. Fixtures

Fixtures provide reusable setup and teardown
functionality for test cases.

Example:

```python
import pytest

@pytest.fixture
def sample_data():
    return [10, 20, 30]

def test_sample_data(sample_data):
    assert len(sample_data) == 3
```

### Fixture Scope

| Scope | Description |
|---|---|
| function | Runs once for each test function |
| class | Runs once for each test class |
| module | Runs once per test module |
| session | Runs once per test session |

### Setup and Teardown using yield

```python
import pytest

@pytest.fixture
def resource():
    print("Setup")

    yield

    print("Teardown")
```

Code before `yield` performs setup.
Code after `yield` performs teardown.

## 6. Test Design Techniques

### Boundary Value Analysis (BVA)

Tests values at and around the boundaries of
an input range.

Example: Password length must be 5–10 characters.

| Input | Expected Result |
|---|---|
| 4 characters | Invalid |
| 5 characters | Valid |
| 6 characters | Valid |
| 9 characters | Valid |
| 10 characters | Valid |
| 11 characters | Invalid |

### Equivalence Partitioning (EP)

Divides input values into groups expected to
behave similarly.

For the same password rule:

- Below 5 characters: Invalid partition
- 5–10 characters: Valid partition
- Above 10 characters: Invalid partition

## 7. Test Reports

Pytest supports report generation through plugins.

Install pytest-html:

```bash
pip install pytest-html
```

Generate an HTML report:

```bash
python -m pytest --html=report.html --self-contained-html
```

The report contains test results and execution details.

## 8. Test Coverage and Negative Testing

### Positive Testing

Verifies that the application behaves correctly
with valid input.

Example:
- Valid username and password.

### Negative Testing

Verifies that the application handles invalid
input correctly.

Example:
- Incorrect password.
- Empty username.
- Missing required fields.

### Deliberate Defect Testing

Temporarily introducing a defect helps verify
whether a test can detect the problem.

The original application code should be restored
after the experiment.

## 9. Python Testing Projects

Practical exercises completed:

### Login Validation

- Username and password validation.
- Positive and negative test cases.
- Parameterized testing.

### Password Validation

- Minimum and maximum password length.
- Boundary Value Analysis.
- Equivalence Partitioning.

### Calculator Testing

- Arithmetic operation validation.
- Input validation.
- Handling invalid input types.
- Excluding Boolean values from integer validation.

## 10. Key Takeaways

- Pytest simplifies Python test automation.
- Assertions verify expected behaviour.
- Parameterization improves test coverage.
- Fixtures support reusable setup and teardown.
- BVA and EP help identify important test inputs.
- Positive and negative tests cover different scenarios.
- HTML reports provide test execution evidence.
