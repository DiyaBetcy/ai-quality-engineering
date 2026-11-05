
from pathlib import Path
from playwright.sync_api import expect


def test_dynamic_message(page):

    file_path = (
        Path(__file__).resolve().parents[1]
        / "app"
        / "dynamic.html"
    )

    page.goto(file_path.as_uri())

    load_button = page.locator("#load-button")
    message = page.locator("#message")

    # Initially, the message should be hidden
    expect(message).to_be_hidden()

    # Click the button
    load_button.click()

    # Wait until the message becomes visible
    expect(message).to_be_visible()

    # Verify the message
    expect(message).to_have_text(
        "Content loaded successfully!"
    )

    reports_dir = Path(__file__).resolve().parents[1] / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Capture screenshot
    screenshot_path = reports_dir / "dynamic_message.png"

    page.screenshot(
        path=str(screenshot_path),
        full_page=True
    )

    print(f"Screenshot saved at: {screenshot_path}")
