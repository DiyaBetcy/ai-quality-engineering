
# Web Automation Using Playwright

## 1. Introduction to Web Automation

Web automation testing uses scripts and tools to
interact with web applications and verify their behaviour.

Playwright is a browser automation framework that
supports Chromium, Firefox and WebKit.

It can automate browser actions such as:

- Opening webpages
- Clicking buttons
- Filling input fields
- Selecting dropdown options
- Checking checkboxes
- Selecting radio buttons
- Validating page content

## 2. Tools and Technologies

- Python
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Chromium
- VS Code

## 3. Installation and Setup

Install Playwright:

```bash
pip install playwright
```

Install Pytest integration:

```bash
pip install pytest-playwright
```

Install HTML reporting:

```bash
pip install pytest-html
```

Install Chromium:

```bash
python -m playwright install chromium
```

## 4. Browser Navigation

Example:

```python
def test_open_homepage(page):

    page.goto("https://www.wikipedia.org/")

    assert page.title() == "Wikipedia"
```

Important methods:

| Method | Purpose |
|---|---|
| page.goto() | Navigate to a URL |
| page.title() | Get page title |
| page.url | Get current URL |
| page.reload() | Reload the webpage |

The `page` fixture is provided by pytest-playwright.

## 5. Locators

Locators identify elements on a webpage.

### Common Locator Methods

| Locator | Purpose |
|---|---|
| get_by_role() | Locate by accessible role |
| get_by_text() | Locate by text |
| get_by_label() | Locate by associated label |
| locator() | Locate using CSS or XPath |

### CSS Selectors

| Selector | Meaning |
|---|---|
| #username | Element with ID username |
| .login-button | Element with class login-button |
| input | Input elements |
| input[type='password'] | Password input |

Example:

```python
username = page.locator("#username")
username.fill("admin")
```

## 6. Browser Interactions

### Fill Input

```python
page.locator("#username").fill("admin")
```

### Click Button

```python
page.get_by_role(
    "button",
    name="Login"
).click()
```

### Select Dropdown

```python
dropdown = page.locator("#dropdown")
dropdown.select_option("1")
```

### Check Checkbox

```python
checkbox = page.locator(
    "input[type='checkbox']"
).nth(0)

checkbox.check()
```

### Uncheck Checkbox

```python
checkbox.uncheck()
```

### Select Radio Button

```python
radio = page.locator("#html")
radio.check()
```

## 7. Assertions

Playwright provides `expect()` for validating
webpage behaviour.

Import:

```python
from playwright.sync_api import expect
```

Examples:

```python
expect(page).to_have_title("Wikipedia")

expect(
    page.locator("#message")
).to_be_visible()

expect(
    page.locator("#username")
).to_have_value("admin")

expect(
    page.locator("#message")
).to_have_text("Login successful!")
```

### Python assert vs Playwright expect

| Python assert | Playwright expect |
|---|---|
| Checks condition immediately | Automatically retries supported assertions |
| General Python assertion | Browser-oriented assertion |
| Does not automatically wait | Waits up to its configured timeout |

## 8. Waiting Mechanisms

Modern webpages often load content dynamically.

Playwright supports condition-based waiting.

| Method | Purpose |
|---|---|
| expect(locator).to_be_visible() | Wait for visibility |
| locator.wait_for() | Wait for a locator state |
| page.wait_for_url() | Wait for URL change |
| page.wait_for_timeout() | Wait for a fixed duration |

Prefer condition-based waiting over fixed delays.

## 9. Dynamic Element Testing

A dynamic element may appear or change after
a user action or a delay.

Example:

```python
load_button = page.locator("#load-button")
message = page.locator("#message")

expect(message).to_be_hidden()

load_button.click()

expect(message).to_be_visible()

expect(message).to_have_text(
    "Content loaded successfully!"
)
```

This verifies that the message becomes visible
after clicking the button.

## 10. Handling Iframes

An iframe is a webpage embedded inside another webpage.

Playwright can locate elements inside an iframe
using frame_locator().

Example:

```python
frame = page.frame_locator("#iframeResult")

html_radio = frame.locator("#html")

html_radio.check()

expect(html_radio).to_be_checked()
```

## 11. Page Object Model (POM)

Page Object Model is a design pattern used to
separate webpage locators and actions from test logic.

### Advantages

- Reusable page methods.
- Less duplicate code.
- Easier maintenance.
- Better separation of responsibilities.

Example:

```python
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("#username")
        self.password = page.locator("#password")

        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

        self.message = page.locator("#message")

    def open(self):
        self.page.goto(self.login_url)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
```

## 12. Screenshot Capture

Screenshots provide visual evidence of application
behaviour and test execution.

Example:

```python
page.screenshot(
    path="playwright/reports/screenshot.png",
    full_page=True
)
```

Use pathlib to create report directories
and construct file paths reliably.

## 13. Automatic Screenshots on Failure

Pytest hooks can capture screenshots automatically
when a test fails.

Implemented using:

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )
```

The implementation is maintained in conftest.py.

Note: This implementation captures failures during
the test execution phase.

## 14. HTML Test Reports

Install:

```bash
pip install pytest-html
```

Generate a self-contained HTML report:

```bash
python -m pytest playwright/tests/ -v --html=playwright/reports/report.html --self-contained-html
```

The report displays:

- Total test count
- Passed tests
- Failed tests
- Skipped tests
- Execution duration
- Test case details

## 15. Playwright Trace Viewer

Trace Viewer helps investigate browser test execution.

Record traces for all test outcomes:

```bash
python -m pytest playwright/tests/test_dynamic.py --tracing=on
```

Retain traces only on failure:

```bash
python -m pytest playwright/tests/test_dynamic.py --tracing=retain-on-failure
```

Open a trace:

```bash
python -m playwright show-trace "path/to/trace.zip"
```

Trace Viewer provides:

- Browser action timeline
- DOM snapshots
- Network activity
- Screenshots
- Test execution details

## 16. Running Playwright Tests

Run all tests:

```bash
python -m pytest playwright/tests/ -v
```

Run tests with a visible browser:

```bash
python -m pytest playwright/tests/ -v --headed
```

Run one test file:

```bash
python -m pytest playwright/tests/test_login.py -v
```

## 17. Practical Exercises Completed

- Browser navigation and homepage testing.
- Wikipedia search automation.
- Input field testing.
- Dropdown selection.
- Checkbox selection and deselection.
- Radio button testing inside an iframe.
- Login positive and negative testing.
- Page Object Model implementation.
- Dynamic element handling.
- Condition-based waiting.
- Screenshot capture.
- Automatic failure screenshots.
- HTML report generation.
- Trace recording.

## 18. Test Execution Results

Latest complete test suite:

| Metric | Result |
|---|---:|
| Total tests | 13 |
| Passed | 13 |
| Failed | 0 |
| Skipped | 0 |
| Execution time | 38 seconds |

## 19. Key Takeaways

- Playwright automates browser interactions.
- Locators identify webpage elements.
- Assertions verify expected behaviour.
- Condition-based waits improve test reliability.
- POM improves maintainability.
- Screenshots and traces support debugging.
- HTML reports provide execution evidence.
