import requests
from .endpoint_manager import EndpointManager


class Requester(EndpointManager):
    def __init__(self, API_KEY="05d52d8812a548c6a9f6f29ed60e8e00"):
        super().__init__()
        self.API_KEY = API_KEY
        self.headers = {'X-Auth-Token': self.API_KEY}
        self.r = object

    def request(self, endpoint_name, payload=None, raw=False):
        if payload is None:
            payload = {}
        url = self.endpoints[endpoint_name]
        self.r = requests.get(url, headers=self.headers, params=payload)
        if raw:
            return self.r
        return self.r.json()
