def validate_numbers(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or isinstance(a,bool) or isinstance(b,bool):
        raise TypeError("Both inputs must be numbers (int or float).")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b


def divide(a, b):
    validate_numbers(a, b)
    return a / b