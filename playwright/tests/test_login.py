
import sys
from pathlib import Path

# Add the playwright folder to Python's import path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_successful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("admin", "12345")

    expect(login_page.message).to_have_text(
        "Login successful!"
    )


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("admin", "wrongpassword")

    expect(login_page.message).to_have_text(
        "Invalid username or password!"
    )
