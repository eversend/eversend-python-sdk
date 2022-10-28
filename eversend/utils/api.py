from __future__ import absolute_import
import json
from requests import request, exceptions
from cachetools import cached, TTLCache

from eversend.utils.exceptions import EversendError

class API(object):
    BASE_URL = 'https://api.eversend.co/'

    def __init__(self, client_id=None, client_secret=None, version='v1'):
        if not client_id or not client_secret:
            raise ValueError('client_id and client_secret required')
        self._client_id = client_id
        self._client_secret = client_secret
        self._version = version
        self._base_url = self.BASE_URL+version
    
    @cached(cache=TTLCache(maxsize=1024, ttl=1600))
    def get_auth_token(self):
        response = request(
            method='GET',
            url=self._base_url+'/auth/token',
            headers={'clientId': self._client_id,
            'clientSecret': self._client_secret})
        token = response.json()['token']
        return token

    def call_api(self, path, method='GET', params=None, data=None):
        token = self.get_auth_token()
        print(token)
        url = self._base_url+path
        headers = {
            'authorization': 'Bearer '+token
        }
        try:
            response = request(
                method=method, url=url, params=params, data=data, headers=headers)
            response.raise_for_status()
            return response.json()['data']
        except exceptions.HTTPError as err:
            raise EversendError(err.response.json()['message'])