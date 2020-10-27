import requests

import config

class Server:
    """\
    A class to representing the gulag server.
    """

    @staticmethod
    def getOnline() -> int:
        """\
        Gets and prints the server's online players.

        Returns
        -------
        int
            A int representing the server's online players.
        """
        request = requests.get(f"https://{config.api_url}/api/get_online").json()
        return request["online"]