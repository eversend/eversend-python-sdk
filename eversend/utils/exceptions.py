class EversendError(Exception):
    def __init__(self, message):
        super(EversendError, self).__init__(message)
