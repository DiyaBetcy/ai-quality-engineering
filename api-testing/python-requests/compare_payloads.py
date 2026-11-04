import requests

url = "https://httpbin.org/post"

payload = {
    "title": "Learning API Testing",
    "userId": 1
}

# JSON request
json_response = requests.post(url, json=payload)

print("JSON Content-Type:")
print(json_response.request.headers["Content-Type"])

print("\nJSON Request Body:")
print(json_response.request.body)


# Form-encoded request
form_response = requests.post(url, data=payload)

print("\nForm Content-Type:")
print(form_response.request.headers["Content-Type"])

print("\nForm Request Body:")
print(form_response.request.body)