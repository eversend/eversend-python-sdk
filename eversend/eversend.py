from eversend import CLIENT_ID, CLIENT_SECRET
from utils.configs import cache
from eversend_wallets import Wallets

class Eversend:
    def __init__(self, client_id, client_secret):
        cache.set(CLIENT_ID, client_id)
        cache.set(CLIENT_SECRET, client_secret)

        classes = (Wallets)

        for _class in classes:
            attr = _class(client_id, client_secret)
            setattr(self, _class.__name__, attr)