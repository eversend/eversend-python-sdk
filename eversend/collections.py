from __future__ import absolute_import
from eversend.utils.api import API

class Collections(API):
    def __init__(self, client_id, client_secret, version):
        super(Collections, self).__init__(client_id, client_secret, version)
    
    def getFees(self, method=None, currency=None, amount=None):
        if not method:
            raise ValueError('method required')
        if not currency:
            raise ValueError('currency required')
        if not amount:
            raise ValueError('amount required')
        payload = {'method': method, 'currency': currency, 'amount': amount }
        return self.call_api(path='/collections/fees', method='POST', data=payload)

    def getOTP(self, phone):
        if not phone:
            raise ValueError('phone required')
        payload = { 'phone': phone }
        return self.call_api(path='/collections/otp', method='POST', data=payload)
    
    def initiate(
            self,
            method=None, 
            phone=None, 
            currency=None, 
            country=None, 
            amount=None, 
            pin=None, 
            pinId=None, 
            transactionRef=None, 
            customer=None
        ):
        if not method:
            raise ValueError('method required')
        if not phone:
            raise ValueError('phone required')
        if not currency:
            raise ValueError('currency required')
        if not country:
            raise ValueError('country required')
        if not amount:
            raise ValueError('amount required')
        payload = {
            'phone': phone,
            'currency': currency,
            'country': country,
            'amount': amount
        }
        if transactionRef is not None:
            payload['transactionRef'] = transactionRef
        if customer is not None:
            payload['customer'] = customer
        if pin is not None and pinId is not None:
            payload['otp'] = {'pin': pin, 'pinId': pinId}
        return self.call_api(path='/collections/'+method, method='post', data=payload)
