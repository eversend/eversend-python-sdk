from wallets import Wallets
class Eversend:
    def __init__(self, client_id, client_secret):
        classes = (Wallets)
        for _class in classes:
            attr = _class(client_id, client_secret)
            setattr(self, _class.__name__, attr)