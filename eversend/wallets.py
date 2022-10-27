from __future__ import absolute_import
from eversend.api import API 
class Wallets(API):
    def __init__(self, client_id, client_secret):
        super(self, Wallets.__init__(client_id, client_secret))
    
    def list(self):
        wallets = self.call_api(path='wallets', method='GET')
        return wallets

    def get(self, currency):
        wallet = self.call_api(path='wallets/'+currency, method='GET')
        return wallet