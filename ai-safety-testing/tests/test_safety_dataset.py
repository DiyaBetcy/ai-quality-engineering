
import json
from pathlib import Path

DATASET_PATH = (
    Path(__file__).resolve().parents[1]
    / "datasets"
    / "safety_testcases.json"
)


def load_safety_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_dataset_is_not_empty():
    dataset = load_safety_dataset()
    assert len(dataset) > 0


def test_each_case_has_required_fields():
    dataset = load_safety_dataset()

    required_fields = {
        "id",
        "category",
        "input",
        "expected_behavior",
        "risk_level"
    }

    for test_case in dataset:
        assert required_fields.issubset(test_case.keys())


def test_test_case_ids_are_unique():
    dataset = load_safety_dataset()

    ids = [test_case["id"] for test_case in dataset]

    assert len(ids) == len(set(ids))


def test_risk_levels_are_valid():
    dataset = load_safety_dataset()

    valid_risk_levels = {"Low", "Medium", "High"}

    for test_case in dataset:
        assert test_case["risk_level"] in valid_risk_levels


def test_dataset_contains_six_scenarios():
    dataset = load_safety_dataset()

    assert len(dataset) == 6
