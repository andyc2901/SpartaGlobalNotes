# API learning
import json
import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req)
print(post_codes_req.json())  # returns a python dict, not an actual json file or string
print(type(post_codes_req.json()))
print(post_codes_req.status_code)
print(post_codes_req.headers)
print(post_codes_req.content)


print(post_codes_req.json()['result']['postcode'])

# Bulk lookup postcodes

headers = {'Content-Type': 'application/json'}
json_data = json.dumps({'postcodes': ["OX49 5NU", "M32 0JG", "NE30 1DP", "NR1 4PZ"]})

post_codes_req2 = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_data)

print('\n')
print(post_codes_req2)
print(post_codes_req2.json())
print(post_codes_req2.json()['result'][0]['result']['country'])

