import json

class ConfigProvider:
    def __init__(self, config_path='config/config.json'):
        with open(config_path) as f:
            self.config = json.load(f)

    def get_base_url(self):
        return self.config['base_url']

    def get_api_url(self):
        return self.config['api_url']

    def get_browser(self):
        return self.config['browser']

    def get_user_credentials(self):
        return self.config['user']['email'], self.config['user']['password']
