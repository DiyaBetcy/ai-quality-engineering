import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.calculator import add, subtract, multiply, divide


def test_addition():
    assert add(10, 5) == 15


def test_subtraction():
    assert subtract(10, 5) == 5


def test_multiplication():
    assert multiply(10, 5) == 50


def test_division():
    assert divide(10, 5) == 2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_addition_with_negative_numbers():
    assert add(-10, 5) == -5


def test_addition_with_zero():
    assert add(10, 0) == 10


def test_multiplication_with_zero():
    assert multiply(10, 0) == 0


def test_division_with_decimal_result():
    assert divide(5, 2) == 2.5