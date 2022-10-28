from __future__ import absolute_import
from eversend.utils.api import API

class Account(API):
    def __init__(self, client_id, client_secret, version):
        super(Account, self).__init__(client_id, client_secret, version)
    
    def getProfile(self):
        wallets = self.call_api(path='/account', method='GET')
        return wallets