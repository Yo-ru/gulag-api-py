""" Import modules. """
import requests

""" Import config. """
import config

__all__ = (
    "Server"
)

class Server:
    """\
    A class representing the gulag server.
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