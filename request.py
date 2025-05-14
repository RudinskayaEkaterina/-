import requests

url = "http://127.0.0.1:8080/rpc"
headers = {
    "X-Client-ID": "sirius-frontend",
    "X-Client-Secret": "my-secret-key",
    "X-Rpc-Method": "math.sum",
    "Content-Type": "application/json"
}
data = {"a": 20, "b": 10}

response = requests.post(url, headers=headers, json=data)
print(response.text())