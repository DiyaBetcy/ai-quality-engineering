import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url, timeout=10)
    return response