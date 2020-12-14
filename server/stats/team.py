import nba_api.stats.endpoints.commonteamroster as tr
import nba_api.stats.endpoints.teamgamelog as info
import nba_api.stats.static.teams as t
from . import base
from pprint import pprint


class Team(base.DataObject):
    def __init__(self, nick_name="", city="", team_id=""):
        super().__init__()
        if nick_name != "":
            self._data = t.find_teams_by_nickname(nick_name)[0]
        elif city != "":
            self._data = t.find_teams_by_city(city)[0]
        elif team_id != "":
            self._data = t.find_team_name_by_id(team_id)[0]

        if self._data == {}:
            raise("Could not instantiate team")

        # pprint(info.TeamGameLog(self['id'], season="2019-20").get_normalized_dict())
        # self._data = info.TeamGameLog(self['id'], season="2019-20").get_normalized_dict()     