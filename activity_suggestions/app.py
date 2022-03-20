from flask import Flask
from flask_restful import Api, Resource, reqparse
import logging
from activity_suggestions.activities import Activities
from activity_suggestions.city import City, get_cities_list


def create_app():
    app = Flask(__name__, static_folder='../react_frontend/build', static_url_path="/")
    app.config['TRAP_HTTP_EXCEPTIONS']=True
    app.config['PROPAGATE_EXCEPTIONS']=True
    
    api = Api(app)

    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
    
    activities = Activities()

    class GetCitiesList(Resource):
        """Get a list of 

        Args:
            Resource (_type_): _description_
        """        
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("city", required=True)            
            args = parser.parse_args()
            response = get_cities_list(args["city"])
            app.logger.info(f"Cities list: {response}")
            return response

    class GetActivitiesByCity(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("city", required=True)
            parser.add_argument("state", required=True)
            parser.add_argument("country", required=True)
            args = parser.parse_args()
            city = City(args["city"],args["state"],args["country"])
            response = {"city": city.city_name, 
            "weather": city.weather, 
            "activities": activities.get_activity_by_suggested_weather(city.weather)}
            app.logger.info(f"Activities by city for {args}: {response}")
            return response

    class GetActivitiesByWeather(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("weather", required=True)
            args = parser.parse_args()
            response = {"activities": activities.get_activity_by_suggested_weather(args["weather"])}
            app.logger.info(f"Activities by weather for {args}: {response}")
            return response

    class GetActivitiesByParticipansNumber(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("participants_number", required=True)
            args = parser.parse_args()
            response = {"activities": activities.get_activity_by_participants_number(int(args["participants_number"]))}
            app.logger.info(f"Activities by participants number for {args}: {response}")
            return response

    class GetActivitiesByCost(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("cost", required=True)
            args = parser.parse_args()
            response = {"activities": activities.get_activity_by_cost(args["cost"])}
            app.logger.info(f"Activities by cost for {args}: {response}")
            return response

    class GetActivitiesUniqueValues(Resource):
        def post(self):
            response = {"activities_weather": sorted(activities.unique_weather),
            "activities_participants_number": sorted(activities.participants_number), 
            "activities_costs":sorted(activities.costs)}
            app.logger.info(f"Activities unique values: {response}")
            return response

    class GetIndex(Resource):
        def get(self):
            app.logger.info("Static homepage loaded.")
            return app.send_static_file("index.html")

    api.add_resource(GetCitiesList, "/citieslist")
    api.add_resource(GetActivitiesUniqueValues, "/getactivitiesuiniquevalues")
    api.add_resource(GetActivitiesByCity, "/getactivitiesbycity")
    api.add_resource(GetActivitiesByWeather, "/getactivitiesbyweather")
    api.add_resource(GetActivitiesByParticipansNumber, "/getactivitiesbyparticipantsnumber")
    api.add_resource(GetActivitiesByCost, "/getactivitiesbycost")
    api.add_resource(GetIndex,"/")


    @app.errorhandler(Exception) 
    def handle_server_error(e):
        app.logger.error(e)
        return str(e), 500

    @app.errorhandler(ValueError) 
    def handle_value_error(e):
        app.logger.error(e)
        return str(e), 404
    
    return app

app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0")