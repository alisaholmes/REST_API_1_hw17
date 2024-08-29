import json

import requests
from jsonschema import validate

from utils.resource import path

endpoint = '/api/users'
endpoint_register = '/api/register'
schema_create_users = path('create_users.json')
schema_register_user = path('register_user.json')
schema_register_unsuccessful = path('register_unsuccessful.json')

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

payload_unsuccessful = {
    "email": "sydney@fife",
}


def test_create_user(base_url):
    response = requests.post(base_url + endpoint, data={"name": "morpheus", "job": "leader"})
    body = response.json()
    assert response.status_code == 201
    with open(schema_create_users) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_register_user(base_url):
    response = requests.post(base_url + endpoint_register, data=payload)
    body = response.json()
    assert response.status_code == 200
    assert response.json()['id'] == 4
    assert response.json()['token']
    with open(schema_register_user) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_register_unsuccessful(base_url):
    error = 'Missing password'
    response = requests.post(base_url + endpoint_register, data=payload_unsuccessful)
    body = response.json()
    assert response.status_code == 400
    assert response.json()['error'] == error
    with open(schema_register_unsuccessful) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
