import requests

import config

class Server:
    @staticmethod
    def getOnline() -> int:
        request = requests.get(f"https://{config.api_url}/api/get_online").json()
        return request["online"]