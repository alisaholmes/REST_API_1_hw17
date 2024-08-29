import json

import requests
from jsonschema import validate

from utils.resource import path

endpoint_post = '/api/users'
endpoint_update_user = '/api/users/'
schema_update_user = path('update_user.json')

payload_post = {
    "name": "morpheus",
    "job": "leader"
}

payload_put = {
    "name": "morpheus",
    "job": "zion resident"
}

update_job = 'zion resident'


def test_put_user(base_url):
    response = requests.post(base_url + endpoint_post, data=payload_post)
    body = response.json()
    update = requests.put(base_url + endpoint_update_user + body['id'], data=payload_put)
    assert update.status_code == 200
    assert update.json()['job'] == update_job
    with open(schema_update_user) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
