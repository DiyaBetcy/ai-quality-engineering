import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.password import validate_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("abcd", False),          # Invalid partition
        ("abcdef", True),         # Valid partition
        ("abcdefghijk", False),   # Invalid partition
    ]
)
def test_password_equivalence(password, expected):
    assert validate_password(password) is expected