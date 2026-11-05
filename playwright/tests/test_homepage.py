from playwright.sync_api import expect


def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login")

    username_field = page.locator("#username")
    password_field = page.locator("#password")

    username_field.fill("tomsmith")
    password_field.fill("SuperSecretPassword!")

    page.locator("button[type='submit']").click()

    expect(page.locator("#flash")).to_contain_text(
        "You logged into a secure area!"
    )

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

def test_invalid_login(page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("wrongpassword")

    page.locator("button[type='submit']").click()

    expect(page.locator("#flash")).to_contain_text(
        "Your password is invalid!"
    )

    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/login"
    )