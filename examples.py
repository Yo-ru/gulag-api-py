""" Import objects. """
from player import Player
from server import Server

# Player example:
print("Player:")

""" player = Player(Union[int, str]) """
player = Player(1)
player = Player("Aika")

""" player.getID() """ 
print(f"ID: {player.getID()}")

""" player.getPP(mode) """
print(f"PP: {player.getPP(0)}")

""" player.getTotalScore(mode) """
print(f"Total Score: {player.getTotalScore(0)}")

""" player.getRankedScore(mode) """
print(f"Ranked Score: {player.getRankedScore(0)}")

""" player.getPlays(mode) """
print(f"Plays: {player.getPlays(0)}")

""" player.getPlayTime(mode) """
print(f"Playtime: {player.getPlayTime(0)}")

""" player.getAcc(mode) """
print(f"Accuracy: {player.getAcc(0)}")

""" player.getMaxCombo(mode) """
print(f"Max Combo: {player.getMaxCombo(0)}")

# Server example.
print("\nServer:")

""" Server.getOnline() """
print(f"Online Users: {Server.getOnline()}")
