import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from api.posts import get_post


def test_get_post_status_code():
    response = get_post(1)

    assert response.status_code == 200


def test_get_post_user_id():
    response = get_post(1)
    data = response.json()

    assert data["userId"] == 1


def test_get_post_id():
    response = get_post(1)
    data = response.json()

    assert data["id"] == 1


def test_get_post_contains_title_and_body():
    response = get_post(1)
    data = response.json()

    assert "title" in data
    assert "body" in data


def test_get_invalid_post():
    response = get_post(999999)

    assert response.status_code == 404