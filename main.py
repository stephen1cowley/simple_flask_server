from flask import Flask, jsonify, request
import requests
import json

url = 'http://127.0.0.1:5000'

# GET
get_response = requests.request('GET', f'{url}/api/data')

payload = {
    "name": "Jane Doe",
    "age": 25,
    "city": "Los Angeles"
}
headers = {
    'content-type': "application/json"
    }


# POST
post_response = requests.request("POST", f'{url}/api/data',
                            data=json.dumps(payload), headers=headers)


print(get_response.json(), post_response.json())
