
# Software Testing

## 1. Introduction to Software Testing

Software testing is the process of verifying and validating a
software application to identify defects and ensure that it
meets the specified requirements.

### Objectives

- Identify defects before software release.
- Verify that requirements are implemented correctly.
- Validate application functionality.
- Improve software quality and reliability.
- Reduce the risk of software failures.

## 2. Verification and Validation

| Verification | Validation |
|---|---|
| Are we building the product right? | Are we building the right product? |
| Checks work products against requirements | Checks whether the product meets user needs |
| Includes reviews and inspections | Includes software testing |

## 3. Software Testing Life Cycle (STLC)

STLC describes the different phases involved in
the software testing process.

1. Requirement Analysis
2. Test Planning
3. Test Case Design
4. Test Environment Setup
5. Test Execution
6. Test Cycle Closure

### Test Execution

During test execution:

- Execute test cases.
- Compare actual and expected results.
- Mark test cases as Pass or Fail.
- Report defects.
- Perform retesting and regression testing.

## 4. Levels of Testing

| Testing Level | Description |
|---|---|
| Unit Testing | Tests individual components or functions |
| Integration Testing | Tests interactions between components |
| System Testing | Tests the complete application |
| Acceptance Testing | Checks whether the application meets user requirements |

## 5. Types of Testing

### Functional Testing

Checks whether application features work according
to the specified requirements.

Examples:
- Login testing
- Registration testing
- Form validation
- Search functionality

### Non-Functional Testing

Evaluates quality attributes of the application.

Examples:
- Performance testing
- Security testing
- Usability testing
- Accessibility testing
- Compatibility testing

## 6. Important Testing Types

### Smoke Testing
A preliminary test to verify that critical application
features work after a new build.

### Sanity Testing
A focused check to verify that a specific change or
fix works as expected.

### Regression Testing
Checks whether new changes have affected previously
working functionality.

### Retesting
Tests a previously failed test case again after the
defect has been fixed.

### Exploratory Testing
Tests an application by exploring its functionality
without relying entirely on predefined test cases.

## 7. Test Case Documentation

A test case describes the steps, conditions and
expected results used to verify a particular feature.

### Common Test Case Fields

| Field | Description |
|---|---|
| Test Case ID | Unique identifier |
| Test Scenario | Feature or functionality being tested |
| Preconditions | Conditions required before execution |
| Test Steps | Actions performed by the tester |
| Test Data | Input values |
| Expected Result | Expected application behaviour |
| Actual Result | Observed application behaviour |
| Status | Pass or Fail |

## 8. Defect Reporting

A defect is an error or issue that causes the
application to behave differently from the expected result.

### Common Bug Report Fields

- Bug ID
- Bug Title
- Environment
- Preconditions
- Steps to Reproduce
- Expected Result
- Actual Result
- Severity
- Priority
- Screenshots or Evidence
- Defect Status

### Severity vs Priority

| Severity | Priority |
|---|---|
| Measures the impact of a defect | Indicates how urgently it should be fixed |
| Technical impact | Business or scheduling urgency |

## 9. Test Design Techniques

### Equivalence Partitioning (EP)

Divides input data into groups expected to behave
similarly.

Example:

A password must contain 5–10 characters.

- Below 5 characters: Invalid partition
- 5–10 characters: Valid partition
- Above 10 characters: Invalid partition

### Boundary Value Analysis (BVA)

Tests values at and around the boundaries of an
input range.

For a password length of 5–10 characters:

| Test Value | Expected Result |
|---|---|
| 4 | Invalid |
| 5 | Valid |
| 6 | Valid |
| 9 | Valid |
| 10 | Valid |
| 11 | Invalid |

## 10. Manual Testing vs Automation Testing

| Manual Testing | Automation Testing |
|---|---|
| Tests are executed manually | Tests are executed using scripts and tools |
| Useful for exploratory testing | Useful for repetitive test execution |
| Requires manual effort | Reduces repetitive effort |
| Can be time-consuming for regression | Enables faster repeated regression |

## Key Takeaways

- Software testing improves application quality.
- STLC provides a structured testing process.
- Test cases document verification steps.
- Defect reports communicate issues clearly.
- BVA and EP help design effective test cases.
- Regression testing checks for unintended side effects.
