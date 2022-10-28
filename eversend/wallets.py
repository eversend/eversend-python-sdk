from __future__ import absolute_import
from eversend.utils.api import API
class Wallets(API):
    def __init__(self, client_id, client_secret, version):
        super(Wallets, self).__init__(client_id, client_secret, version)
    
    def list(self):
        wallets = self.call_api(path='/wallets', method='GET')
        return wallets

    def getOne(self, currency):
        wallet = self.call_api(path='/wallets/'+currency, method='GET')
        return wallet