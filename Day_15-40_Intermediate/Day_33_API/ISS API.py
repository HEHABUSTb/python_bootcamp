import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

code = response.status_code
response.raise_for_status()
assert code == 200, f"Status code not equal 200 actual status code '{code}'"

data = response.json()
print(data)