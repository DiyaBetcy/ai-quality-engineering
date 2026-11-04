import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# Request details
print("Status Code:", response.status_code)
print("Response Time:", response.elapsed.total_seconds())

# Response body
data = response.json()

print("\nResponse Data:")
print(data)

# Individual JSON fields
print("\nIndividual Fields:")
print("User ID:", data["userId"])
print("Post ID:", data["id"])
print("Title:", data["title"])
print("Body:", data["body"])

assert response.status_code == 200

assert data["userId"] == 1
assert data["id"] == 1

assert "title" in data
assert "body" in data

print("\nAll API validations passed!")