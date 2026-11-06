
# API Testing

## 1. Introduction to API Testing

API testing verifies whether application programming
interfaces work correctly, reliably and securely.

An API allows different software applications to
communicate with each other.

API testing focuses on requests, responses, status
codes, headers, authentication and data validation.

## 2. Client-Server Communication

Basic API communication involves:

1. Client sends an HTTP request.
2. Server processes the request.
3. Server returns an HTTP response.
4. Client receives and processes the response.

Example:

Client -> GET /posts/1 -> Server
Client <- JSON response <- Server

## 3. HTTP Methods

HTTP methods define the operation requested from an API.

| Method | Purpose |
|---|---|
| GET | Retrieve information |
| POST | Create or submit information |
| PUT | Replace an existing resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

### GET Example

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)

print(response.status_code)
print(response.json())
```

### POST Example

```python
payload = {
    "title": "Learning API Testing",
    "body": "Practising API requests",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,
    timeout=10
)

print(response.status_code)
print(response.json())
```

## 4. HTTP Status Codes

Status codes indicate the result of an HTTP request.

| Status Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

Status codes should be validated according
to the API requirements.

## 5. API Request and Response

### Request

An HTTP request can contain:

- URL or endpoint
- HTTP method
- Headers
- Query parameters
- Request body
- Authentication details

### Response

An HTTP response can contain:

- Status code
- Response headers
- Response body
- Response time

## 6. JSON Payloads

JSON is a commonly used format for exchanging
data between clients and servers.

Example:

```json
{
    "title": "API Testing",
    "body": "Learning Python Requests",
    "userId": 1
}
```

Using Requests:

```python
response = requests.post(
    url,
    json=payload,
    timeout=10
)
```

The `json` parameter serializes the Python dictionary
into JSON and sets the appropriate Content-Type header.

## 7. Headers

Headers provide additional information about
HTTP requests and responses.

Common headers:

| Header | Purpose |
|---|---|
| Accept | Specifies acceptable response formats |
| Content-Type | Indicates the request body format |
| Authorization | Carries authentication credentials |

### JSON vs Form Data

Using `json=payload` sends JSON data.

Using `data=payload` with a Python dictionary
typically sends form-encoded data.

Common content types:

- application/json
- application/x-www-form-urlencoded

## 8. Query Parameters

Query parameters filter or modify API requests.

Example:

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
    timeout=10
)
```

This requests posts belonging to user ID 1.

## 9. Authentication and Authorization

### Authentication

Verifies the identity of a user or client.

### Authorization

Determines what an authenticated user
or client is allowed to access.

### HTTP Basic Authentication

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://httpbin.org/basic-auth/user/pass",
    auth=HTTPBasicAuth("user", "pass"),
    timeout=10
)

print(response.status_code)
```

Common authentication approaches include:

- Basic Authentication
- API Keys
- Bearer Tokens
- OAuth 2.0

## 10. Positive and Negative API Testing

### Positive Testing

Checks API behaviour with valid requests.

Examples:
- Retrieve an existing post.
- Create a post with valid fields.
- Update an existing resource.

### Negative Testing

Checks API behaviour with invalid requests.

Examples:
- Invalid resource ID.
- Missing required fields.
- Invalid credentials.
- Incorrect data types.
- Malformed request body.

Expected behaviour should be based on API requirements.

## 11. Error Handling

API requests can fail because of:

- Connection errors
- Request timeouts
- Server errors
- Invalid responses

Example:

```python
import requests

try:
    response = requests.get(
        "https://httpbin.org/delay/10",
        timeout=2
    )

    print(response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Connection error!")
```

Timeouts prevent a test from waiting indefinitely
for a response.

## 12. API Testing Using Pytest

Pytest can automate API validation.

Example:

```python
import requests


def test_get_post():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
```

### Parameterized API Testing

```python
import pytest
import requests


@pytest.mark.parametrize(
    "user_id",
    [1, 2, 3, 4]
)
def test_posts_by_user(user_id):

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": user_id},
        timeout=10
    )

    assert response.status_code == 200

    posts = response.json()

    assert all(
        post["userId"] == user_id
        for post in posts
    )
```

## 13. API Testing Tools

### Python Requests

A Python library used to send HTTP requests
and handle API responses.

### Postman

A graphical tool for sending API requests,
examining responses and organizing collections.

## 14. Practical Project

### JSONPlaceholder API Testing

Practice API:
https://jsonplaceholder.typicode.com

Implemented operations:

- GET a post
- POST a post
- PUT a post
- PATCH a post
- DELETE a post
- Retrieve posts using query parameters

Additional exercises:

- HTTP Basic Authentication using httpbin.
- Request timeout handling.
- Header inspection.
- JSON and form-data comparison.
- Positive and negative API testing.
- Parameterized API tests.

Note: JSONPlaceholder simulates write operations.
POST, PUT, PATCH and DELETE requests do not
persistently modify its underlying dataset.

## 15. Key Takeaways

- API testing validates communication between applications.
- HTTP methods represent different operations.
- Status codes indicate request outcomes.
- Headers provide request and response metadata.
- Query parameters help filter API data.
- Authentication and authorization serve different purposes.
- Requests supports API automation using Python.
- Pytest enables repeatable API test execution.
- Positive and negative testing improve API coverage.
- Timeouts and exception handling improve test reliability.
