from flask import Flask
from flask_restful import Api, Resource, reqparse
from activity_suggestions.activities import Activities
from activity_suggestions.city import City, get_cities_list

def create_app():
    app = Flask(__name__, static_folder='../react_frontend/build', static_url_path="/")
    app.config['TRAP_HTTP_EXCEPTIONS']=True

    api = Api(app)

    activities = Activities()

    class GetCitiesList(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("city", required=True)            
            args = parser.parse_args()
            return get_cities_list(args["city"])

    class GetActivities(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("city", required=True)
            parser.add_argument("state", required=True)
            parser.add_argument("country", required=True)
            args = parser.parse_args()
            city = City(args["city"],args["state"],args["country"])
            return city.__dict__, activities.get_activity_by_suggested_weather(city.weather)

    class GetIndex(Resource):
        def get(self):
            return app.send_static_file("index.html")

    api.add_resource(GetCitiesList, "/city")
    api.add_resource(GetActivities, "/activities")
    api.add_resource(GetIndex,"/")

    @app.errorhandler(Exception) 
    def handle_server_error(e):
        print(e)
        return str(e), 500

    @app.errorhandler(ValueError) 
    def handle_value_error(e):
        print(e)
        return str(e), 404
    
    return app

app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0")