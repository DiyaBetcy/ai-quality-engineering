import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.login import validate_login


@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("admin", "12345", True),
        ("admin", "wrong", False),
        ("user", "12345", False),
        ("", "12345", False),
        ("admin", "", False),
        ("", "", False),
        ("guest", "guest123", False),
        ("ADMIN", "12345", False),
        ("Admin","12345",False),
        ("aDMIN","12345", False)
    ]
)
def test_login_scenarios(username, password, expected):
    assert validate_login(username, password) is expected