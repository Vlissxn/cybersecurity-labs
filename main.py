import requests

response = requests.get("https://httpbin.org/ip", timeout=10)

print("Status:", response.status_code)
print("Informações de IP:", response.json())