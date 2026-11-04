import requests

url = "https://httpbin.org/delay/5"

try:
    response = requests.get(url, timeout=2)

    print("Status:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Unable to connect to the server!")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)