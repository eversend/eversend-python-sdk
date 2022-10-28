from __future__ import absolute_import
from eversend.utils.api import API

class Beneficiaries(API):
    def __init__(self, client_id, client_secret, version):
        super(Beneficiaries, self).__init__(client_id, client_secret, version)
    
    def list(self, page=1, limit=10, search=None, type=None):
        params = {'page': page, 'limit': limit}
        if search is not None:
            params['search'] = search
        if type is not None:
            params['type'] = type
        return self.call_api(path='/beneficiaries?', params=params, method='GET')

    def getOne(self, beneficiaryId):
        if not beneficiaryId:
            raise ValueError('beneficiaryId required')
        return self.call_api(path='/beneficiaries/'+str(beneficiaryId), method='GET')
    
    def create(self, beneficiaries=None):
        if not beneficiaries:
            raise ValueError('beneficiaries object required')
        return self.call_api(path='/beneficiaries', method='POST', data=beneficiaries)
    
    def update(
            self, 
            beneficiaryId=None, 
            firstName=None, 
            lastName=None,
            phoneNumber=None,
            bankName=None,
            bankCode=None,
            bankAccountName=None,
            bankAccountNumber=None,
        ):
        if not beneficiaryId:
            raise ValueError('beneficiaryId required')
        payload = {}
        if firstName is not None:
            payload['firstName'] = firstName
        if lastName is not None:
            payload['lastName'] = lastName
        if phoneNumber is not None:
            payload['phoneNumber'] = phoneNumber
        if bankName is not None:
            payload['bankName'] = bankName
        if bankCode is not None:
            payload['bankCode'] = bankCode
        if bankAccountName is not None:
            payload['bankAccountName'] = bankAccountName
        if bankAccountNumber is not None:
            payload['bankAccountNumber'] = bankAccountNumber
        return self.call_api(path='/beneficiaries/'+str(beneficiaryId), method='PUT', data=payload)
    
    def delete(self, beneficiaryId):
        if not beneficiaryId:
            raise ValueError('beneficiaryId required')
        return self.call_api(path='/beneficiaries/'+str(beneficiaryId), method='DELETE')
    
    def checkBankDetails(self, countryCode, bankCode, accountNumber):
        payload = {'countryCode': countryCode, 'bankCode': bankCode, 'accountNumber': accountNumber}
        return self.call_api(path='/beneficiaries/accounts/banks', method='POST', data=payload)
    
    def hasEversendAccount(self, phone):
        if not phone:
            raise ValueError('phone required')
        return self.call_api(path='/beneficiaries/accounts/eversend', method='POST', data={'phone': phone})['accountExists']
