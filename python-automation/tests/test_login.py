import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.login import validate_login


def test_valid_login():
    assert validate_login("admin", "12345") is True


def test_invalid_password():
    assert validate_login("admin", "wrong") is False


def test_empty_username():
    assert validate_login("", "12345") is False


def test_empty_password():
    assert validate_login("admin", "") is False