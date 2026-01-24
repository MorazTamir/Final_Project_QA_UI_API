import requests

class ClientWrapper:
    def __init__(self):
        self._session = requests.Session()

    def get(self, url, params=None, headers=None):
        return self._session.get(url, params=params, headers=headers)

    def post(self, url, data=None, json=None, headers=None):
        return self._session.post(url, data=data, json=json, headers=headers)

    def put(self, url, data=None, json=None, headers=None):
        return self._session.put(url, data=data, json=json, headers=headers)

    def delete(self, url, headers=None):
        return self._session.delete(url, headers=headers)