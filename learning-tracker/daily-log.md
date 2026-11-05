## Defect Detection Exercise

- Introduced an intentional password-validation defect.
- Executed the automated test suite.
- Pytest identified the incorrect login behaviour.
- One test failed and three passed.
- Analysed expected versus actual results.
- Restored the correct implementation and retested.

## Day 2 – Pytest Advanced Concepts

- Practised parameterized testing using `pytest.mark.parametrize`.
- Learned fixtures and fixture scopes.
- Implemented setup and teardown using `yield`.
- Practised Boundary Value Analysis (BVA).
- Practised Equivalence Partitioning (EP).
- Generated an HTML test execution report using pytest-html.
- Final test result: 20 passed.

## Day 3 – Python Automation Testing

- Practised Pytest assertions.
- Tested expected exceptions using pytest.raises().
- Performed positive and negative testing.
- Tested different input data types.
- Implemented reusable input validation.
- Practised defect injection and regression testing.
- Final test result: 35 passed.

## Day 4 – API Testing Fundamentals

- Learned API and REST API fundamentals.
- Practised HTTP methods: GET, POST, PUT, PATCH and DELETE.
- Understood HTTP status codes.
- Used Python Requests to send API requests.
- Validated JSON response data and headers.
- Practised positive and negative API testing.
- Learned Pytest fixtures in API automation.
- Handled connection errors and request timeouts.
- Generated HTML API test reports.
- Final result: 13 passed, 0 failed.

## Day 5 – Advanced API Testing

- Practised query parameters in API requests.
- Learned parameterized testing using pytest.mark.parametrize.
- Tested multiple valid and invalid inputs.
- Understood positive and negative API testing.
- Learned HTTP request headers: Accept, Content-Type and Authorization.
- Compared JSON and form-encoded payloads using json= and data=.
- Practised Basic Authentication using HTTPBasicAuth.
- Automated valid and invalid authentication tests.
- Learned HTTP 401 and HTTP 500 responses.
- Practised handling timeout and connection exceptions.
- Used try-except for API error handling.


# Day 6 - Playwright Web Automation

## Objective
Learn browser automation using Playwright with Python and Pytest.

## Topics Covered

- Browser automation using Chromium
- Navigating webpages
- Locating elements using Playwright locators
- Filling text fields and clicking buttons
- Dropdown selection
- Checkbox and radio button interactions
- Assertions using Playwright expect()
- Handling iframes
- Page Object Model (POM)

## Project Structure

playwright/
├── app/
│   └── login.html
├── pages/
│   └── login_page.py
├── tests/
│   ├── test_homepage.py
│   ├── test_inputs.py
│   ├── test_dropdown.py
│   ├── test_checkboxes.py
│   ├── test_radio.py
│   └── test_login.py
└── README.md

## Page Object Model

Implemented a LoginPage class to separate webpage
locators and actions from test scenarios.

The page object contains:
- Username locator
- Password locator
- Login button locator
- Login message locator
- open() method
- login() method

## Login Test Scenarios

| Test Case | Expected Result |
|---|---|
| Valid username and password | Login successful |
| Valid username and invalid password | Invalid credentials message |

Practice credentials:
- Username: admin
- Password: 12345

Note: The local login application is a frontend-only
practice application.

## Execution

Run all Playwright tests:

python -m pytest playwright/tests/ -v

Run login tests in headed mode:

python -m pytest playwright/tests/test_login.py -v --headed

## Key Learning

Page Object Model improves maintainability by
separating page interactions from test logic.


## Day 7 – Advanced Playwright Automation

**Status:** Completed (Trace Viewer exploration pending, if not yet verified)

### Topics Covered

1. **Dynamic Element Handling**
   - Tested elements that appear after a delay.
   - Used Playwright assertions to wait for elements.
   - Understood condition-based waits versus fixed waits.

2. **Screenshot Capture**
   - Captured webpage screenshots using `page.screenshot()`.
   - Created report directories dynamically using `pathlib`.
   - Verified screenshot file generation.

3. **Automatic Screenshots on Test Failure**
   - Created a shared Pytest configuration using `conftest.py`.
   - Implemented `pytest_runtest_makereport` hook.
   - Captured screenshots automatically when test execution failed.
   - Verified automatic failure screenshot generation.

4. **HTML Test Reports**
   - Used `pytest-html` to generate HTML reports.
   - Examined test execution results, duration, and failure details.
   - Generated a self-contained HTML report.

5. **Playwright Trace Recording**
   - Learned trace recording using Playwright.
   - Used `--tracing=retain-on-failure`.
   - Used `--tracing=on` to record successful test executions.
   - Located the generated `trace.zip` file.
   - Learned how to open traces using Playwright Trace Viewer.

### Practical Work

- Created `dynamic.html` for dynamic content testing.
- Created `test_dynamic.py`.
- Implemented condition-based assertions.
- Captured manual screenshots.
- Implemented automatic failure screenshots in `conftest.py`.
- Generated HTML test reports.
- Recorded browser execution traces.

### Test Results

**Latest complete Playwright test suite:**

| Metric | Result |
|---|---:|
| Total tests | 13 |
| Passed | 13 |
| Failed | 0 |
| Skipped | 0 |
| Execution time | 38 seconds |

Dynamic element test: Passed.

Automatic failure screenshot: Successfully generated.

### Important Concepts Learned

- Dynamic elements and asynchronous page behaviour.
- Explicit condition-based waiting.
- Pytest hooks and shared fixtures.
- Screenshot evidence collection.
- HTML test reporting.
- Browser execution traces and debugging.

### Key Takeaway

Advanced Playwright automation helps make browser tests more reliable
and maintainable. Screenshots, HTML reports, and execution traces
provide useful evidence for investigating application failures.
