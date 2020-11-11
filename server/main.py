import flask

def build_routes(app):
    data = {}
    data['Hi'] = "yoyoyoy"


    @app.route('/', methods=['GET'])
    def home():
        return data

    


if __name__ == "__main__":
    
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    build_routes(app)
    app.run()