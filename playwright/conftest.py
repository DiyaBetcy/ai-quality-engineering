
from pathlib import Path
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only when the test execution fails
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            reports_dir = (
                Path(__file__).resolve().parent / "reports"
            )
            reports_dir.mkdir(
                parents=True, exist_ok=True
            )

            screenshot_path = (
                reports_dir / f"{item.name}_failure.png"
            )

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            print(
                f"\nFailure screenshot: {screenshot_path}"
            )
