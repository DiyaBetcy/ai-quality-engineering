import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url, timeout=10)
    return response

def create_post(title, body, user_id):
    url = f"{BASE_URL}/posts"

    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(url, json=payload, timeout=10)

    return response