
# Playwright Web Automation

## Overview

This module contains hands-on browser automation exercises using
Playwright with Python and Pytest.

The objective is to understand browser interactions, element
locators, assertions, dynamic content handling, screenshots,
test reports, and debugging.

## Tools and Technologies

- Python 3.14
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Chromium
- VS Code

## Project Structure

playwright/
├── app/
│   ├── login.html
│   └── dynamic.html
├── pages/
│   └── login_page.py
├── tests/
│   ├── test_homepage.py
│   ├── test_inputs.py
│   ├── test_dropdown.py
│   ├── test_checkboxes.py
│   ├── test_radio.py
│   ├── test_login.py
│   └── test_dynamic.py
├── reports/
│   ├── dynamic_message.png
│   └── report.html
├── conftest.py
└── README.md

## Topics Covered

### 1. Browser Automation

- Launching Chromium through Pytest.
- Navigating webpages using page.goto().
- Accessing page titles and URLs.
- Understanding the Playwright page fixture.

### 2. Locators and Browser Interactions

- get_by_role()
- get_by_text()
- get_by_label()
- locator()
- CSS selectors
- fill()
- click()
- check() and uncheck()
- select_option()

### 3. Assertions

Used Playwright's expect() assertions to verify:

- Element visibility.
- Text content.
- Input values.
- Checkbox and radio button states.
- Page titles and URLs.

### 4. Page Object Model (POM)

Implemented a LoginPage class to separate page
locators and actions from test scenarios.

The page object contains:

- Username locator
- Password locator
- Login button locator
- Login message locator
- open() method
- login() method

Used pathlib to construct the local HTML file URL
dynamically instead of hardcoding the computer-specific path.

### 5. Dynamic Element Testing

Created a local HTML application that displays a
message three seconds after clicking a button.

Verified:

- Initial hidden state.
- Button interaction.
- Dynamic message visibility.
- Expected message content.

Used condition-based assertions instead of fixed waits.

### 6. Screenshot Capture

Used page.screenshot() to capture browser screenshots.

Implemented:

- Manual screenshot capture.
- Screenshot directory creation using pathlib.
- Automatic screenshots when test execution fails.

Automatic failure screenshots are implemented using
the pytest_runtest_makereport hook in conftest.py.

### 7. HTML Test Reports

Used pytest-html to generate an HTML test report.

Command:

python -m pytest playwright/tests/ -v --html=playwright/reports/report.html --self-contained-html

The report provides:

- Total test count.
- Passed and failed tests.
- Execution duration.
- Test case details.

### 8. Playwright Trace Viewer

Learned how to record browser execution traces.

Record traces even for passing tests:

python -m pytest playwright/tests/test_dynamic.py --tracing=on

Retain traces only when tests fail:

python -m pytest playwright/tests/test_dynamic.py --tracing=retain-on-failure

Open a trace:

python -m playwright show-trace "path/to/trace.zip"

Trace Viewer helps inspect browser actions, DOM snapshots,
network activity, and execution details.

## Test Results

Latest complete Playwright test suite:

| Metric | Result |
|---|---:|
| Total tests | 13 |
| Passed | 13 |
| Failed | 0 |
| Skipped | 0 |
| Execution time | 38 seconds |

Note: Results reflect the test run on 5 November 2026.

## Local Practice Applications

### Login Application

Credentials:

- Username: admin
- Password: 12345

This is a frontend-only practice application,
not a production authentication system.

### Dynamic Content Application

Displays a message after a three-second delay
when the user clicks the Load Message button.

## Running Tests

Run all Playwright tests:

python -m pytest playwright/tests/ -v

Run a specific test:

python -m pytest playwright/tests/test_login.py -v

Run tests with a visible browser:

python -m pytest playwright/tests/ -v --headed

Generate an HTML report:

python -m pytest playwright/tests/ -v --html=playwright/reports/report.html --self-contained-html

## Key Learnings

- Browser automation using Playwright.
- Reliable element identification.
- Condition-based waiting.
- Page Object Model.
- Positive and negative test scenarios.
- Dynamic element handling.
- Screenshot evidence collection.
- Automated failure screenshots.
- HTML test reporting.
- Browser execution tracing and debugging.
