from playwright.sync_api import expect


def test_select_dropdown(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown = page.locator("#dropdown")

    dropdown.select_option("1")

    expect(dropdown).to_have_value("1")