import sys
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR / "app"))

from evaluator import (
    evaluate_response,
    load_dataset,
    DATASET_PATH
)


def test_correctness_pass():
    item = {
        "expected_answer": "Guido van Rossum",
        "evaluation_metric": "correctness"
    }

    result = evaluate_response(
        item,
        "Python was developed by Guido van Rossum."
    )

    assert result is True


def test_correctness_fail():
    item = {
        "expected_answer": "Guido van Rossum",
        "evaluation_metric": "correctness"
    }

    result = evaluate_response(
        item,
        "Python was developed by James Gosling."
    )

    assert result is False


def test_instruction_following_pass():
    item = {
        "expected_answer": "Two relevant bullet points",
        "evaluation_metric": "instruction_following"
    }

    response = (
        "- Python is a programming language.\n"
        "- Python is used in AI."
    )

    assert evaluate_response(item, response) is True


def test_instruction_following_fail():
    item = {
        "expected_answer": "Two relevant bullet points",
        "evaluation_metric": "instruction_following"
    }

    response = "- Python is a programming language."

    assert evaluate_response(item, response) is False


def test_faithfulness_pass():
    item = {
        "expected_answer": "9 AM to 5 PM",
        "context": "The library is open from 9 AM to 5 PM.",
        "evaluation_metric": "faithfulness"
    }

    response = "The library is open from 9 AM to 5 PM."

    assert evaluate_response(item, response) is True


def test_faithfulness_fail():
    item = {
        "expected_answer": "9 AM to 5 PM",
        "context": "The library is open from 9 AM to 5 PM.",
        "evaluation_metric": "faithfulness"
    }

    response = "The library is open from 10 AM to 6 PM."

    assert evaluate_response(item, response) is False


def test_completeness_pass():
    item = {
        "expected_answer": "An explanation of HTML and two uses",
        "evaluation_metric": "completeness"
    }

    response = (
        "HTML is used to structure web pages "
        "and create forms and links."
    )

    assert evaluate_response(item, response) is True


def test_completeness_fail():
    item = {
        "expected_answer": "An explanation of HTML and two uses",
        "evaluation_metric": "completeness"
    }

    response = "HTML is used to create web pages."

    assert evaluate_response(item, response) is False

def test_dataset_loads_successfully():
    dataset = load_dataset()

    assert dataset is not None
    assert isinstance(dataset, list)


def test_dataset_contains_five_records():
    dataset = load_dataset()

    assert len(dataset) == 5