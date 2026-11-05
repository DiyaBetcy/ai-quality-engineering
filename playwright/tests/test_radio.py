from playwright.sync_api import expect


def test_radio_button(page):
    page.goto(
        "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_radio"
    )

    frame = page.frame_locator("#iframeResult")

    html_radio = frame.locator("#html")
    css_radio = frame.locator("#css")

    html_radio.check()
    expect(html_radio).to_be_checked()

    css_radio.check()
    expect(css_radio).to_be_checked()

    expect(html_radio).not_to_be_checked()