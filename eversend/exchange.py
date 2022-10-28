from __future__ import absolute_import
from eversend.utils.api import API

class Exchange(API):
    def __init__(self, client_id, client_secret, version):
        super(Exchange, self).__init__(client_id, client_secret, version)
    
    def getQuotation(self, source=None, destination=None, amount=None):
        if not source:
            raise ValueError('method required')
        if not destination:
            raise ValueError('currency required')
        if not amount:
            raise ValueError('amount required')
        payload = {'from': source, 'to': destination, 'amount': amount }
        return self.call_api(path='/exchanges/quotation', method='post', data=payload)
    
    def exchange(
            self,
            token=None,
        ):
        if not token:
            raise ValueError('method required')
        payload = {
            'token': token
        }
        return self.call_api(path='/exchanges', method='post', data=payload)
