from infra.API.base_api import BaseApi

class CaontactApi():

    @staticmethod
    def get_messages():
        return BaseApi.get_api_call(f'messages')

    @staticmethod
    def get_message_by_id(message_id):
        return BaseApi.get_api_call(f'messages/{message_id}')

    @staticmethod
    def post_messages(payload):
        return BaseApi.post_api_call(f'messages', payload)

    @staticmethod
    def post_messages_file(message_id, payload): #we want empty
        return BaseApi.post_api_call(f'messages/{message_id}/attach-file', payload)

    @staticmethod
    def post_messages_reply(message_id, payload):
        return BaseApi.post_api_call(f'messages/{message_id}/reply', payload)

    @staticmethod
    def put_status_messages(message_id, payload):
        return BaseApi.put_api_call(f'messages/{message_id}/status', payload)