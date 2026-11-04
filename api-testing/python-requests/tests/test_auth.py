import requests
from requests.auth import HTTPBasicAuth


URL = "https://httpbin.org/basic-auth/user/pass"


def test_valid_credentials():
    response = requests.get(
        URL,
        auth=HTTPBasicAuth("user", "pass"),
        timeout=10
    )

    assert response.status_code == 200
    assert response.json()["authenticated"] is True


def test_invalid_credentials():
    response = requests.get(
        URL,
        auth=HTTPBasicAuth("user", "wrong"),
        timeout=10
    )

    assert response.status_code == 401