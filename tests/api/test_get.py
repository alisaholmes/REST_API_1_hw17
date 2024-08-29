import json

import requests
from jsonschema import validate

from utils.resource import path

endpoint = '/api/users/2'
endpoint_not_found = '/api/users/23'
endpoint_negative_single_resource = '/api/unknown/none'
schema_single_users = path('single_user.json')


def test_single_user_acquisition(base_url):
    response = requests.get(base_url + endpoint)
    body = response.json()
    assert response.status_code == 200
    with open(schema_single_users) as file:
        validate(body, schema=json.loads(file.read()))


def test_single_user_not_found(base_url):
    response = requests.get(base_url + endpoint_not_found)
    assert response.status_code == 404
    assert response.json() == {}


def test_negative_single_resource(base_url):
    response = requests.get(base_url + endpoint_negative_single_resource)
    assert response.status_code == 404
    assert response.json() == {}
