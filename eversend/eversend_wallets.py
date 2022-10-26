from utils.http import call_api

class Wallets:
    def __init__(self, client_id, client_secret):
        pass
    
    def list(self):
        wallets = call_api(path='wallets', method='GET')
        return wallets

    def get(self, currency):
        wallet = call_api(path='wallets/'+currency, method='GET')
        return wallet