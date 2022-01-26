import json

class CORSHeaders:
    """Return the data and the errors from validating `instance` against `schema`."""
    def __init__(self, origin: str = None, credentials: bool = False):
        self.origin = origin or '*'
        self.credentials = credentials

    def buildHeaders(self):
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': self.origin
        }
        if self.credentials:
            headers['Access-Control-Allow-Credentials'] = True
        return headers
