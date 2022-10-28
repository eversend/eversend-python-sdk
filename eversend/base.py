from eversend.wallets import Wallets
from eversend.transactions import Transactions
from eversend.collections import Collections
from eversend.account import Account
from eversend.exchange import Exchange
from eversend.beneficiaries import Beneficiaries
from eversend.payouts import Payouts
from eversend.crypto import Crypto

class Eversend:
    def __init__(self, client_id, client_secret, version='v1'):
        classes = (
            Wallets, Transactions, Collections, Account, Exchange, Beneficiaries, Payouts, Crypto
        )
        for _class in classes:
            attr = _class(client_id, client_secret, version)
            setattr(self, _class.__name__, attr)