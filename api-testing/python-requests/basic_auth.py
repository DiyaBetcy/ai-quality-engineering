import requests
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/pass"

response = requests.get(
    url,
    auth=HTTPBasicAuth("user", "wrong"),
    timeout=10
)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Response:", response.json())

elif response.status_code == 401:
    print("Authentication failed!")
    print("Response:", response.text)

else:
    print("Unexpected response:", response.text)