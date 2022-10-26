from __future__ import absolute_import
from requests import request
from configs import cache
from eversend import CLIENT_ID, CLIENT_SECRET, BASE_URL, TOKEN

def get_auth_token():
    token = cache.get(TOKEN)
    if not token:
        client_id = cache.get(CLIENT_ID)
        client_secret = cache.get(CLIENT_SECRET)
        response = request(
            method='GET',
            url=BASE_URL+'/auth/token',
            headers={'clientId': client_id,
            'clientSecret': client_secret})
        token = response.json['data']['token']

    return token

def call_api(path, method='GET', params=None, data=None):
    token = get_auth_token
    url = BASE_URL+path
    headers = {
        'authorization': 'Bearer '+token
    }
    response = request(
        method=method, url=url, params=params, data=data, headers=headers)
    return response.json['data']