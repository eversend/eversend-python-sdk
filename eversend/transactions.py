from __future__ import absolute_import
from eversend.utils.api import API

class Transactions(API):
    def __init__(self, client_id, client_secret, version):
        super(Transactions, self).__init__(client_id, client_secret, version)
    
    def list(self, page=1, limit=10):
        params = {'page': page, 'limit': limit}
        return self.call_api(path='/transactions?', params=params, method='GET')

    def getOne(self, transactionId):
        return self.call_api(path='/transactions/'+transactionId, method='GET')