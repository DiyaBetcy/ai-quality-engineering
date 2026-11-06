
import json
from pathlib import Path


# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

# JSON dataset location
DATASET_PATH = (
    PROJECT_DIR / "datasets" / "evaluation_dataset.json"
)


def load_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        dataset = json.load(file)

    return dataset


if __name__ == "__main__":
    data = load_dataset()

    print(f"Total evaluation records: {len(data)}")

    for item in data:
        print(
            item["id"],
            "|",
            item["question"],
            "|",
            item["evaluation_metric"]
        )
