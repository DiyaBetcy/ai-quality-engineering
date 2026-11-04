import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.password import validate_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("abcd", False),       # Minimum - 1
        ("abcde", True),       # Minimum
        ("abcdef", True),      # Minimum + 1
        ("abcdefghi", True),   # Maximum - 1
        ("abcdefghij", True), # Maximum
        ("abcdefghijk", False) # Maximum + 1
    ]
)
def test_password_length(password, expected):
    assert validate_password(password) is expected