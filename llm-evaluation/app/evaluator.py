
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_DIR / "datasets" / "evaluation_dataset.json"


def load_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# Simulated AI responses for practice
def generate_response(test_id):
    responses = {
        "LLM001": "Python was developed by Guido van Rossum.",
        "LLM002": "CPU stands for Central Processing Unit.",
        "LLM003": (
            "- Python is a high-level programming language.\n"
            "- Python is used in web development, automation and AI."
        ),
        "LLM004": "The library is open from 9 AM to 5 PM.",
        "LLM005": (
            "HTML stands for HyperText Markup Language. "
            "It is used to structure web pages and create "
            "forms and links."
        )
    }

    return responses.get(test_id, "")


def evaluate_response(item, actual_response):
    expected = item["expected_answer"]
    metric = item["evaluation_metric"]

    if metric == "correctness":
        passed = expected.lower() in actual_response.lower()

    elif metric == "instruction_following":
        bullet_count = sum(
            1 for line in actual_response.splitlines()
            if line.strip().startswith(("-", "*"))
        )
        passed = bullet_count == 2

    elif metric == "faithfulness":
        context = item.get("context", "")
        passed = (
            context != ""
            and "9 AM to 5 PM" in actual_response
        )

    elif metric == "completeness":
        response = actual_response.lower()
        passed = (
            "html" in response
            and "structure web pages" in response
            and "forms and links" in response
        )

    else:
        passed = False

    return passed


if __name__ == "__main__":
    dataset = load_dataset()

    total = 0
    passed_count = 0

    print("\n========== LLM EVALUATION RESULTS ==========\n")

    for item in dataset:
        actual_response = generate_response(item["id"])
        result = evaluate_response(item, actual_response)

        total += 1

        if result:
            passed_count += 1

        print("Test ID:", item["id"])
        print("Question:", item["question"])
        print("AI Response:", actual_response)
        print("Metric:", item["evaluation_metric"])
        print("Result:", "PASS" if result else "FAIL")
        print("-" * 50)

    print("\n========== SUMMARY ==========")
    print("Total:", total)
    print("Passed:", passed_count)
    print("Failed:", total - passed_count)
