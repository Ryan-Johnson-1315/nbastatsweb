import nba_api.stats.static.teams as t
import nba_api.stats.endpoints.commonallplayers as c
import nba_api.stats.endpoints


def run():
    # print(t.find_teams_by_nickname("jazz"))
    # print(t.get_teams())

    # for team in t.get_teams():
    #     for key in team:
    #         print(f'{key}: {team[key]}')
    #     print('------------')

    print(c.CommonAllPlayers().get_json())