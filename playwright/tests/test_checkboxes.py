from playwright.sync_api import expect


def test_check_checkbox(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = page.locator("input[type='checkbox']")

    first_checkbox = checkboxes.nth(0)

    first_checkbox.check()

    expect(first_checkbox).to_be_checked()


def test_uncheck_checkbox(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = page.locator("input[type='checkbox']")

    second_checkbox = checkboxes.nth(1)

    second_checkbox.uncheck()

    expect(second_checkbox).not_to_be_checked()