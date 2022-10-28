from __future__ import absolute_import
from eversend.utils.api import API

class Payouts(API):
    def __init__(self, client_id, client_secret, version):
        super(Payouts, self).__init__(client_id, client_secret, version)
    
    def countries(self):
        return self.call_api(path='/payouts/countries', method='GET')['countries']

    def banks(self, country):
        return self.call_api(path='/payouts/banks/'+country, method='GET')
    
    def getQuotation(self, sourceWallet, amount, type, destinationCountry, destinationCurrency, amountType='SOURCE'):
        payload = {
            'sourceWallet': sourceWallet,
            'amount': amount,
            'type': type,
            'destinationCountry': destinationCountry,
            'destinationCurrency': destinationCurrency,
            'amountType': amountType
        }
        return self.call_api(path='/payouts/quotation', method='POST', data=payload)
    
    def initiate(
            self, 
            token,
            beneficiaryId: None,
            phoneNumber: None,
            firstName: None,
            lastName: None,
            country: None,
            bankName=None,
            bankCode=None,
            bankAccountName=None,
            bankAccountNumber=None,
        ):
        payload = {
            'token': token,
        }
        if beneficiaryId is not None:
            payload['beneficiaryId'] = beneficiaryId
        if firstName is not None:
            payload['firstName'] = firstName
        if lastName is not None:
            payload['lastName'] = lastName
        if phoneNumber is not None:
            payload['phoneNumber'] = phoneNumber
        if country is not None:
            payload['country'] = country
        if bankName is not None:
            payload['bankName'] = bankName
        if bankCode is not None:
            payload['bankCode'] = bankCode
        if bankAccountName is not None:
            payload['bankAccountName'] = bankAccountName
        if bankAccountNumber is not None:
            payload['bankAccountNumber'] = bankAccountNumber
        return self.call_api(path='/payouts', method='POST', data=payload)
