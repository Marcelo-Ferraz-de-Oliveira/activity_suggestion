from flask import Flask, request, jsonify
from activity_suggestions.activities import Activities
from activity_suggestions.city import City
app = Flask(__name__, static_folder='../react_frontend/build', static_url_path="/")
app.config['TRAP_HTTP_EXCEPTIONS']=True

activities = Activities()
city = City("Goiânia")

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/a")
def get_month_profit():
    return jsonify(activities.activities[0], activities.unique_weather)

@app.route("/suggested")
def return_suggested_activities():
    return jsonify(city.city_name, city.weather, activities.get_activity_by_suggested_weather(city.weather))

@app.errorhandler(Exception) 
def handle_server_error(e) -> tuple:
    return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0")