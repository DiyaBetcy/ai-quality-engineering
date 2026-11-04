import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from api.posts import get_post, create_post, update_post, patch_post, delete_post


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

def test_create_post():
    response = create_post(
        "Learning API Testing",
        "Practising POST requests using Python",
        1
    )

    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "Learning API Testing"
    assert data["body"] == "Practising POST requests using Python"
    assert data["userId"] == 1
    assert "id" in data

def test_update_post():
    response = update_post(
        1,
        "Updated title",
        "Updated body",
        1
    )

    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Updated title"
    assert data["body"] == "Updated body"


def test_patch_post():
    response = patch_post(1, "Partially updated title")

    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Partially updated title"

def test_delete_post():
    response = delete_post(1)

    assert response.status_code == 200