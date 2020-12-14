from . import base
import nba_api.stats.static.players as p

class Player(base.DataObject):
    def __init__(self, name="", player_id=""):
        super().__init__()
        if name != "":
            self._data = p.find_players_by_full_name(name)[0]
        elif player_id != "":
            self._data = p.find_player_by_id(player_id)[0]

        if self._data == {}:
            raise("Could not instantiate player")
