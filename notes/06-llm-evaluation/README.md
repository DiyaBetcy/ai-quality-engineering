
# LLM Evaluation Framework

A hands-on project demonstrating basic LLM response evaluation using Python, JSON, Pytest and pytest-html.

## 1. Project Overview

This project implements a basic rule-based evaluation framework to assess simulated AI responses against predefined evaluation criteria.

The framework loads evaluation records from a JSON dataset, generates predefined responses, evaluates them using simple rules and produces test execution results.

### Objectives

- Understand the fundamentals of LLM response evaluation.
- Create a structured evaluation dataset.
- Implement rule-based evaluation metrics.
- Perform positive and negative testing.
- Automate evaluation tests using Pytest.
- Generate HTML test reports.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.14 | Implementation |
| JSON | Evaluation dataset |
| Pytest | Automated testing |
| pytest-html | HTML reporting |
| pathlib | File path management |
| VS Code | Development environment |

## 3. Project Structure

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

## 4. Evaluation Dataset

The evaluation dataset contains five records.

Each record includes:

- `id`: Unique evaluation record identifier.
- `question`: Input question or instruction.
- `expected_answer`: Expected answer or evaluation reference.
- `evaluation_metric`: Metric used to evaluate the response.
- `context`: Additional information for context-based evaluation, when applicable.

### Dataset Example

```json
{
    "id": "LLM001",
    "question": "Who developed Python?",
    "expected_answer": "Guido van Rossum",
    "evaluation_metric": "correctness"
}
```

### Evaluation Records

| ID | Question | Evaluation Metric |
|---|---|---|
| LLM001 | Who developed Python? | Correctness |
| LLM002 | What does CPU stand for? | Correctness |
| LLM003 | Explain Python in exactly two bullet points. | Instruction Following |
| LLM004 | What are the library timings? | Faithfulness |
| LLM005 | Explain HTML and mention two uses. | Completeness |

## 5. Evaluation Metrics Implemented

### 5.1 Correctness

Checks whether the expected answer appears in the actual response.

Example:

- Expected: Guido van Rossum
- Actual: Python was developed by Guido van Rossum.
- Result: PASS

### 5.2 Instruction Following

Checks whether the response follows the requested output format.

Example:

Instruction: Explain Python in exactly two bullet points.

The current implementation counts lines beginning with `-` or `*` and checks whether exactly two bullet points are present.

### 5.3 Faithfulness

Checks whether the generated response contains information supported by the supplied context.

Example:

Context: The library is open from 9 AM to 5 PM.

Expected response: 9 AM to 5 PM.

The current implementation checks for the expected timing phrase.

### 5.4 Completeness

Checks whether the response contains the required information.

Example:

Instruction: Explain HTML and mention two uses.

The current implementation checks for:
- HTML
- Structure web pages
- Forms and links

## 6. Evaluator Implementation

Main file:

`app/evaluator.py`

The implementation contains three main functions.

### load_dataset()

Loads the evaluation records from the JSON file using Python's `json` module.

### generate_response()

Returns predefined simulated responses based on the evaluation record ID.

These responses are used for practicing the evaluation process.

### evaluate_response()

Evaluates the response based on the metric specified in the dataset.

The current implementation uses simple rule-based checks.

### Evaluation Workflow

1. Load the JSON evaluation dataset.
2. Retrieve each evaluation record.
3. Generate a simulated response.
4. Identify the applicable evaluation metric.
5. Evaluate the response.
6. Record PASS or FAIL.
7. Calculate the final summary.

## 7. Positive and Negative Testing

Both positive and negative scenarios were tested.

### Positive Testing

Verified that correct or expected responses pass the evaluation rules.

Initial results:

- Total records: 5
- Passed: 5
- Failed: 0

### Negative Testing

Deliberately introduced an incorrect response.

Original response:

```text
Python was developed by Guido van Rossum.
```

Modified response:

```text
Python was developed by James Gosling.
```

The evaluator correctly identified the modified response as a failure.

Negative test results:

- Total records: 5
- Passed: 4
- Failed: 1

After restoring the correct response, all five records passed again.

## 8. Pytest Integration

Created the test file:

`tests/test_evaluation.py`

Independent test cases were implemented for four evaluation metrics.

| Evaluation Metric | Positive Test | Negative Test |
|---|---|---|
| Correctness | Correct answer | Incorrect answer |
| Instruction Following | Exactly two bullet points | One bullet point |
| Faithfulness | Response matches context | Response contradicts context |
| Completeness | Required information included | Required information missing |

Two additional tests were added to validate dataset loading:

- Dataset loads successfully.
- Dataset contains five records.

### Total Test Coverage

| Category | Number of Tests |
|---|---:|
| Correctness | 2 |
| Instruction Following | 2 |
| Faithfulness | 2 |
| Completeness | 2 |
| Dataset Loading | 2 |
| **Total** | **10** |

## 9. Running the Tests

Run all evaluation tests from the repository root:

```bash
python -m pytest llm-evaluation/ -v
```

Expected result:

```text
10 passed
```

## 10. HTML Test Reporting

Used `pytest-html` to generate an HTML test report.

Command:

```bash
python -m pytest llm-evaluation/ -v --html=llm-evaluation/reports/evaluation_report.html --self-contained-html
```

Report location:

`reports/evaluation_report.html`

The report includes:

- Test execution summary.
- Individual test results.
- Execution duration.
- Python and platform information.
- Installed testing plugins.

### Final HTML Report Results

| Metric | Result |
|---|---:|
| Total Tests | 10 |
| Passed | 10 |
| Failed | 0 |
| Skipped | 0 |
| Execution Time | 151 ms |

## 11. Challenges and Resolutions

### Python Module Import Error

**Issue:** Pytest could not locate the `evaluator` module during test collection.

**Error:**

```text
ModuleNotFoundError: No module named 'evaluator'
```

**Resolution:**

Added the application directory to Python's module search path.

```python
PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "app"))
```

This allowed the test file to import the evaluator module successfully.

## 12. Limitations

This project is a basic rule-based evaluation prototype.

Current limitations:

- Uses predefined simulated responses rather than a live LLM.
- Correctness is checked using substring matching.
- Instruction following checks bullet count, not the quality of the content.
- Faithfulness uses a predefined phrase check rather than comprehensive context verification.
- Completeness checks for predefined keywords.
- Does not yet implement semantic similarity, DeepEval or LLM-as-a-Judge.

A passing result means that the response satisfies the implemented rule. It does not guarantee overall response quality.

## 13. Future Improvements

Possible improvements include:

- Integrating a live LLM API.
- Implementing semantic similarity evaluation.
- Exploring DeepEval.
- Implementing LLM-as-a-Judge.
- Evaluating hallucinations.
- Adding AI safety and harmful-content evaluation.
- Improving context-grounded faithfulness checks.

## 14. Key Learnings

- Designing structured LLM evaluation datasets.
- Implementing rule-based evaluation logic.
- Understanding correctness, faithfulness, completeness and instruction following.
- Performing positive and negative testing.
- Writing independent Pytest test cases.
- Testing dataset-loading functionality.
- Resolving Python module import-path issues.
- Generating HTML test reports.
- Understanding the limitations of simple evaluation rules.

## 15. Project Status

**Day 10 – Completed**

- Evaluation dataset: Created.
- Rule-based evaluator: Implemented.
- Negative testing: Verified.
- Pytest integration: Completed.
- Dataset-loading tests: Completed.
- HTML report: Generated and verified.
- Final test result: 10 passed, 0 failed.
