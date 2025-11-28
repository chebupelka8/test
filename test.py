import requests

data = requests.get("http://localhost:8080/users")

print(data.json())