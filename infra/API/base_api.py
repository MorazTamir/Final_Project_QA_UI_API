import requests
from infra.API.response_wrapper import ResponseWrapper

class BaseApi:

    BASE_URL = "https://api.practicesoftwaretesting.com/api"

    @staticmethod
    def get_api_call(endpoint):
        response = requests.get(f"{BaseApi.BASE_URL}/{endpoint}")
        return ResponseWrapper(response.ok, response.status_code, response.json())

    @staticmethod
    def post_api_call(endpoint, payload=None):
        response = requests.post(
            f"{BaseApi.BASE_URL}/{endpoint}",
            json=payload
        )
        return ResponseWrapper(response.ok, response.status_code, response.json())

    @staticmethod
    def put_api_call(endpoint, payload):
        response = requests.put(
            f"{BaseApi.BASE_URL}/{endpoint}",
            json=payload
        )
        return ResponseWrapper(response.ok, response.status_code, response.json())

    @staticmethod
    def delete_api_call(endpoint):
        response = requests.delete(f"{BaseApi.BASE_URL}/{endpoint}")
        return ResponseWrapper(response.ok, response.status_code, response.json())
