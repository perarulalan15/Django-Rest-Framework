import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint, json={"query":"hello world!"})
print(response.text)
print(response.json())
print(response.status_code)