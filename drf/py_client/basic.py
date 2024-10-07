import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/"

response = requests.get(endpoint, json={"query":"hello world!"})
print(response.text)
print(response.status_code)
# print(response.json())