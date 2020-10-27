import requests
from typing import Union

import config

class Player:
    __slots__ = (
        "player",
        "request"
    )

    def __init__(self, player: Union[int, str]) -> None:
        self.player = player

        # Build URL.
        url: str = f"http://{config.api_url}/api/get_stats?"
        if type(self.player) is str:
            url += f"name={self.player}"
        elif type(self.player) is int:
            url += f"id={self.player}"

        # Make request to API.
        self.request = requests.get(url, verify=False)

        # Make sure user exists.
        if self.request.content == b"User not found.":
            raise Exception("Player not found!")

    def getID(self) -> int:
        """ Returns id of Player. """
        return self.request.json()["id"]

    """
    Mode:
    vn!std   = 0
    vn!taiko = 1
    vn!catch = 2
    vn!mania = 3
    rx!std   = 4
    rx!taiko = 5
    rx!catch = 6
    ap!std   = 7
    """

    def getPP(self, mode: int) -> int:
        """ Returns pp for specified mode. """
        if mode == 0:
            return self.request.json()["pp_vn_std"]
        elif mode == 1:
            return self.request.json()["pp_vn_taiko"]
        elif mode == 2:
            return self.request.json()["pp_vn_catch"]
        elif mode == 3:
            return self.request.json()["pp_vn_mania"]
        elif mode == 4:
            return self.request.json()["pp_rx_std"]
        elif mode == 5:
            return self.request.json()["pp_rx_taiko"]
        elif mode == 6:
            return self.request.json()["pp_rx_catch"]
        elif mode == 7:
            return self.request.json()["pp_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

    def getTotalScore(self, mode: int) -> int:
        """ Returns total score for specificed mode. """
        if mode == 0:
            return self.request.json()["tscore_vn_std"]
        elif mode == 1:
            return self.request.json()["tscore_vn_taiko"]
        elif mode == 2:
            return self.request.json()["tscore_vn_catch"]
        elif mode == 3:
            return self.request.json()["tscore_vn_mania"]
        elif mode == 4:
            return self.request.json()["tscore_rx_std"]
        elif mode == 5:
            return self.request.json()["tscore_rx_taiko"]
        elif mode == 6:
            return self.request.json()["tscore_rx_catch"]
        elif mode == 7:
            return self.request.json()["tscore_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

    def getRankedScore(self, mode: int) -> int:
        """ Returns ranked score for specified mode. """
        if mode == 0:
            return self.request.json()["rscore_vn_std"]
        elif mode == 1:
            return self.request.json()["rscore_vn_taiko"]
        elif mode == 2:
            return self.request.json()["rscore_vn_catch"]
        elif mode == 3:
            return self.request.json()["rscore_vn_mania"]
        elif mode == 4:
            return self.request.json()["rscore_rx_std"]
        elif mode == 5:
            return self.request.json()["rscore_rx_taiko"]
        elif mode == 6:
            return self.request.json()["rscore_rx_catch"]
        elif mode == 7:
            return self.request.json()["rscore_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

    def getPlays(self, mode: int) -> int:
        """ Returns plays for specified mode. """
        if mode == 0:
            return self.request.json()["plays_vn_std"]
        elif mode == 1:
            return self.request.json()["plays_vn_taiko"]
        elif mode == 2:
            return self.request.json()["plays_vn_catch"]
        elif mode == 3:
            return self.request.json()["plays_vn_mania"]
        elif mode == 4:
            return self.request.json()["plays_rx_std"]
        elif mode == 5:
            return self.request.json()["plays_rx_taiko"]
        elif mode == 6:
            return self.request.json()["plays_rx_catch"]
        elif mode == 7:
            return self.request.json()["plays_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

    def getPlayTime(self, mode: int) -> int:
        """ Returns playtime for specified mode. """
        if mode == 0:
            return self.request.json()["playtime_vn_std"]
        elif mode == 1:
            return self.request.json()["playtime_vn_taiko"]
        elif mode == 2:
            return self.request.json()["playtime_vn_catch"]
        elif mode == 3:
            return self.request.json()["playtime_vn_mania"]
        elif mode == 4:
            return self.request.json()["playtime_rx_std"]
        elif mode == 5:
            return self.request.json()["playtime_rx_taiko"]
        elif mode == 6:
            return self.request.json()["playtime_rx_catch"]
        elif mode == 7:
            return self.request.json()["playtime_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

    def getAcc(self, mode: int) -> float:
        """ Returns accuracy for specified mode. """
        if mode == 0:
            return self.request.json()["acc_vn_std"]
        elif mode == 1:
            return self.request.json()["acc_vn_taiko"]
        elif mode == 2:
            return self.request.json()["acc_vn_catch"]
        elif mode == 3:
            return self.request.json()["acc_vn_mania"]
        elif mode == 4:
            return self.request.json()["acc_rx_std"]
        elif mode == 5:
            return self.request.json()["acc_rx_taiko"]
        elif mode == 6:
            return self.request.json()["acc_rx_catch"]
        elif mode == 7:
            return self.request.json()["acc_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

    def getMaxCombo(self, mode: int) -> int:
        """ Returns maximum combo for specified mode. """
        if mode == 0:
            return self.request.json()["maxcombo_vn_std"]
        elif mode == 1:
            return self.request.json()["maxcombo_vn_taiko"]
        elif mode == 2:
            return self.request.json()["maxcombo_vn_catch"]
        elif mode == 3:
            return self.request.json()["maxcombo_vn_mania"]
        elif mode == 4:
            return self.request.json()["maxcombo_rx_std"]
        elif mode == 5:
            return self.request.json()["maxcombo_rx_taiko"]
        elif mode == 6:
            return self.request.json()["maxcombo_rx_catch"]
        elif mode == 7:
            return self.request.json()["maxcombo_ap_std"]
        else:
            raise Exception("Invalid mode selected!")

