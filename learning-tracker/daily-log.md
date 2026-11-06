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



# Day 8 – LLM Fundamentals

## Objective
Understand Large Language Models and identify
quality risks in AI-generated responses.

## Topics Learned

- Large Language Models (LLMs)
- Prompts and tokens
- Context windows
- Temperature
- Inference
- Hallucinations
- Conventional software testing vs LLM testing

## LLM Testing Scenarios

| Test ID | Scenario | What to Validate |
|---|---|---|
| LLM-001 | Ask a factual question | Factual accuracy |
| LLM-002 | Ask an ambiguous question | Clarification and relevance |
| LLM-003 | Ask the same question multiple times | Response consistency |
| LLM-004 | Provide a long conversation | Context retention |
| LLM-005 | Ask a question with false information | Resistance to incorrect assumptions |
| LLM-006 | Ask an unrelated question | Relevance |
| LLM-007 | Ask for a concise answer | Instruction following |

## Key Takeaways

- LLMs generate responses based on learned patterns and context.
- The same prompt may produce different responses.
- Hallucinations are an important AI quality risk.
- LLM testing requires evaluating meaning and quality,
  not just exact text matching.




## Day 9 – LLM Evaluation Fundamentals

### Topics Covered
- Introduction to LLM evaluation.
- Difference between conventional software testing and LLM evaluation.
- Evaluation metrics:
  - Correctness
  - Relevance
  - Faithfulness
  - Completeness
  - Coherence
  - Consistency
  - Safety
  - Instruction following
- Reference answers and evaluation datasets.
- Human evaluation and automated evaluation.
- Rule-based evaluation.
- LLM-as-a-Judge approach.

### Practical Learning
- Studied how expected answers can be used to evaluate AI responses.
- Designed evaluation scenarios for factual accuracy, instruction following, context-based answering and completeness.
- Prepared a JSON evaluation dataset for the upcoming implementation.

### Key Learning
LLM evaluation checks not only whether a response is correct, but also whether it is relevant, complete, faithful to the context and follows instructions.

### Status
Completed


# Day 10 – Building an LLM Evaluation Framework

## Objective
Build a basic rule-based LLM evaluation framework using Python and Pytest to evaluate simulated AI responses against predefined evaluation criteria.

## Activities Completed

### Activity 1 – Dataset Loading

- Created the LLM evaluation project structure.
- Prepared a JSON evaluation dataset containing five test records.
- Implemented a dataset-loading function using Python's `json` module.
- Used `pathlib` to construct file paths dynamically.
- Successfully loaded and displayed all five evaluation records.

**File:** `llm-evaluation/app/evaluator.py`

### Activity 2 – Rule-Based Evaluator Implementation

Implemented the following functions:

- `load_dataset()` – Loads evaluation records from the JSON dataset.
- `generate_response()` – Generates predefined simulated AI responses.
- `evaluate_response()` – Evaluates responses using predefined rules.

Implemented four evaluation metrics:

1. **Correctness:** Checks whether the expected answer appears in the actual response.
2. **Instruction Following:** Checks whether the response contains exactly two bullet points.
3. **Faithfulness:** Checks whether the response includes the expected library timings from the context.
4. **Completeness:** Checks whether the response contains the required HTML explanation and two uses.

Executed the evaluator successfully.

**Initial execution results:**
- Total records: 5
- Passed: 5
- Failed: 0

### Activity 3 – Negative Testing

- Deliberately introduced an incorrect response for the Python developer question.
- Changed the response from Guido van Rossum to James Gosling.
- Executed the evaluator to verify whether it detected the incorrect answer.
- Confirmed that the correctness rule identified the response as a failure.
- Restored the original correct response.

**Negative test results:**
- Total records: 5
- Passed: 4
- Failed: 1

After restoring the correct response:
- Passed: 5
- Failed: 0

**Key learning:** Negative testing verifies whether an evaluation system can detect incorrect or unexpected responses.

### Activity 4 – Pytest Integration

Created:

`llm-evaluation/tests/test_evaluation.py`

Implemented independent positive and negative test cases for:

- Correctness
- Instruction following
- Faithfulness
- Completeness

Used assertions to verify the expected evaluation results.

**Test execution command:**

```powershell
python -m pytest llm-evaluation/tests/test_evaluation.py -v
```

**Execution results:**
- Total tests: 8
- Passed: 8
- Failed: 0
- Execution time: 0.11 seconds

### Activity 5 – Dataset Loading Tests

Added independent tests to verify:

- Successful dataset loading.
- Whether the loaded dataset is a list.
- Whether the dataset contains exactly five records.

Encountered a Python module import-path issue during test collection.

Resolved it by adding the application directory to Python's module search path using `sys.path.insert()`.

Executed the complete test suite.

**Test execution command:**

```powershell
python -m pytest llm-evaluation/ -v
```

**Execution results:**
- Total tests: 10
- Passed: 10
- Failed: 0
- Execution time: 0.11 seconds

### Activity 6 – HTML Test Reporting

- Generated an HTML test report using `pytest-html`.
- Saved the report in the project reports directory.
- Opened and verified the generated HTML report.
- Reviewed individual test results, execution duration and environment information.

**Report location:**

`llm-evaluation/reports/evaluation_report.html`

**Execution command:**

```powershell
python -m pytest llm-evaluation/ -v --html=llm-evaluation/reports/evaluation_report.html --self-contained-html
```

**Final HTML report results:**
- Total tests: 10
- Passed: 10
- Failed: 0
- Skipped: 0
- Execution time: 151 ms

## Project Structure

```text
llm-evaluation/
├── datasets/
│   └── evaluation_dataset.json
├── app/
│   └── evaluator.py
├── tests/
│   └── test_evaluation.py
├── reports/
│   └── evaluation_report.html
└── README.md
```

## Tools and Technologies Used

- Python 3.14
- JSON
- Pytest
- pytest-html
- pathlib
- VS Code
- PowerShell

## Key Learnings

- Building a basic rule-based LLM evaluation framework.
- Loading structured evaluation datasets using JSON.
- Separating response generation from evaluation logic.
- Evaluating simulated AI responses against predefined criteria.
- Understanding positive and negative testing.
- Writing independent Pytest test cases.
- Testing dataset-loading functionality.
- Handling Python module import paths.
- Generating and verifying HTML test reports.
- Understanding the importance of testing the evaluation system itself.

## Limitations

- The current framework uses predefined simulated responses rather than a live LLM.
- Evaluation is based on simple keyword and formatting rules.
- Faithfulness and completeness checks are not comprehensive semantic evaluations.
- The current implementation does not use DeepEval or an LLM-as-a-Judge approach.

## Overall Day 10 Results

| Metric | Result |
|---|---:|
| Evaluation dataset records | 5 |
| Pytest test cases | 10 |
| Tests passed | 10 |
| Tests failed | 0 |
| Tests skipped | 0 |
| HTML report | Generated and verified |

**Day 10 Status: COMPLETED**
