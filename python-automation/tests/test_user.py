import pytest


@pytest.fixture
def user():
    print("\nCreating test user")
    return {
        "username": "diya",
        "email": "diya@example.com",
        "role": "tester"
    }


def test_username(user):
    assert user["username"] == "diya"


def test_email(user):
    assert user["email"] == "diya@example.com"


def test_role(user):
    assert user["role"] == "tester"