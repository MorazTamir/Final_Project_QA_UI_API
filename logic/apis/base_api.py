import requests
from infra.response_wrapper import ResponseWrapper
from config.config_provider import ConfigProvider

class BaseApi:
    def __init__(self):
        self.config = ConfigProvider()
        self.base_url = self.config.get_api_url()

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        return ResponseWrapper(response.ok, response.status_code, response.json())

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return ResponseWrapper(response.ok, response.status_code, response.json())
