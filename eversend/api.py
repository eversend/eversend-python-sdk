from __future__ import absolute_import
from requests import request
from cache3 import SafeCache
from eversend import BASE_URL, TOKEN

cache = SafeCache()

class API(object):
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret
    
    def get_auth_token(self):
        token = cache.get(TOKEN)
        if not token:
            response = request(
                method='GET',
                url=BASE_URL+'/auth/token',
                headers={'clientId': self._client_id,
                'clientSecret': self._client_secret})
            token = response.json['data']['token']
            cache.set(TOKEN, token, 1600.0) #compensating for network lags in the timeout
        return token

    def call_api(self, path, method='GET', params=None, data=None):
        token = self.get_auth_token
        url = BASE_URL+path
        headers = {
            'authorization': 'Bearer '+token
        }
        response = request(
            method=method, url=url, params=params, data=data, headers=headers)
        return response.json['data']