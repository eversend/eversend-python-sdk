from __future__ import absolute_import
from eversend.utils.api import API

class Crypto(API):
    def __init__(self, client_id, client_secret, version):
        super(Crypto, self).__init__(client_id, client_secret, version)
    
    def addresses(self, page=1, limit=10):
        params = {'page': page, 'limit': limit}
        return self.call_api(path='/crypto/addresses?', params=params, method='GET')
    
    def transactions(self, page=1, limit=10):
        params = {'page': page, 'limit': limit}
        return self.call_api(path='/crypto/transactions?', params=params, method='GET')

    def getAssetChains(self, coin):
        return self.call_api(path='/crypto/assets/'+coin, method='GET')

    def createAddress(self, assetId, ownerName, destinationAddressDescription, purpose=None,):
        payload={
            'assetId': assetId,
            'ownerName': ownerName,
            'destinationAddressDescription': destinationAddressDescription,
        }
        if purpose is not None:
            payload['purpose'] = purpose
        return self.call_api(path='/crypto/addresses', method='POST', data=payload)