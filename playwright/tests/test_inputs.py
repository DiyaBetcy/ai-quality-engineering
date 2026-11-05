from playwright.sync_api import expect


def test_number_input(page):
    page.goto("https://the-internet.herokuapp.com/inputs")

    number_input = page.locator("input[type='number']")

    number_input.fill("12345")

    expect(number_input).to_have_value("12345")