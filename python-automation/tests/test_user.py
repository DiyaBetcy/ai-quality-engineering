import pytest

@pytest.fixture
def browser():
    print("\nOpening browser")

    yield "Browser is ready"

    print("\nClosing browser")


def test_homepage(browser):
    assert browser == "Browser is ready"