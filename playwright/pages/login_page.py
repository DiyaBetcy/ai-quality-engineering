
from pathlib import Path


class LoginPage:

    def __init__(self, page):
        self.page = page

        # Build the local HTML file path dynamically
        self.login_url = (
            Path(__file__).resolve().parents[1]
            / "app"
            / "login.html"
        ).as_uri()

        # Locators
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.get_by_role(
            "button", name="Login"
        )
        self.message = page.locator("#message")

    def open(self):
        self.page.goto(self.login_url)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
