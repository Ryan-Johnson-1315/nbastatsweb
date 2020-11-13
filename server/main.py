import flask
# import nba
import nba_api.stats.endpoints.playercareerstats as pc
import nba_api.stats.static.players as players

def build_routes(app):
    player = players.find_players_by_full_name('donovan mitchell')[0]
    print(player)
    @app.route('/career', methods=['GET'])
    
    def home():
        data = pc.PlayerCareerStats(player['id']).get_dict()
        
        headers = []
        rowSets   = []
        for f in data['resultSets']:
            for d in f:
                headers = f['headers']
                rowSets = f['rowSet']

        # print('\n\n\n')
        # goingBack = {}
        # for rowSet in rowSets:
        #     for h, d in zip(headers, rowSet):
        #         print(f'{h}: {d}')
        #         goingBack[h] = d
        #     print('\n\n\n')
        
        return {'data': rowSets, 'keys': headers}

if __name__ == "__main__":
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    build_routes(app)
    app.run()

    # nba.run()