import requests
from activity_suggestions.api_key import API_KEY

class City(object):
    """Class to concentrate city information, coordinates and weather.
    It first set city_name, state and country attributes, from API selected result from city passed as contructor argument;
    then set lat and long based on coordinates from API selected result from city_name, state and country attributes;
    and, finally, set weather from API selected result from lat and long attributes.
    
    It gets all information from openweathermap API services. Learn more: https://openweathermap.org/current

    Attributes:
        city_name (str): City name returned from API (can be different from original city variable passed as argument)
        state (str): State where City is in.
        country (str): Contry where City is in.
        lat (float): City latitute.
        lon (float): City longitude.
        weather (str): Weather condition string get in the moment of creation or get_city_weather call
    """    
    def __init__(self, city_name: str, state: str, country: str) -> None:
        """Construtor that populate all attributes with API data.

        Args:
            city (str): City name to get information.
        """              
        self.city_name = city_name
        self.state = state
        self.country = country
        self.lat, self.lon = self._get_citie_coordinate(self.city_name, self.state, self.country)
        self.weather = self.get_city_weather()
    
    def _get_citie_coordinate(self, city_name: str, state: str, country: str) -> list:
        """Get, from API call, the latitude and longitide of first city of correspondent city_name, state and contry object attributes.

        Args:
            city_name (str): city_name object attribute.
            state (str): state object attribute.
            country (str): country object attribute.

        Returns:
            list: list with latitide and longitude.
        """     
        api_call = _string_api_call_coordinates(city_name, state, country, 1)
        cities_result = requests.get(api_call)
        if not cities_result.ok: raise Exception("Error while calling API openweathermap API.")
        if not cities_result.json(): raise ValueError("City not found.")
        result = cities_result.json()[0]
        coordinates = [result["lat"], result["lon"]]
        return coordinates

    def get_city_weather(self) -> str:
        """_summary_

        Raises:
            Exception: Error when API request fails (malformed request, API server error, network error, etc).
            ValueError: Error when API request returns an empty list - wrong coordinates.

        Returns:
            str: Weather in "main" field from first "weather" dict of API result
        """        
        api_call = _string_api_call_weather(self.lon, self.lat)
        weather_result = requests.get(api_call)
        if not weather_result.ok: raise Exception("Error while calling API openweathermap API.")
        if not weather_result.json(): raise ValueError("Wrong coordinates.")
        return weather_result.json()['weather'][0]["main"]

def _string_api_call_coordinates(city: str, state: str = "", country: str = "", limit: int = 5) -> str:
    return f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={API_KEY}"

def _string_api_call_weather(lat: float, lon: float) -> str:
    return f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

def get_cities_list( city: str) -> list:
    """Make an API request to get the first 5 cities information, with name, state and country.

    Args:
        city (str): City string to get information

    Raises:
        Exception: Error when API request fails (malformed request, API server error, network error, etc).
        ValueError: Error when API request returns an empty list - city not found.

    Returns:
        list: Return a list with 1 to 5 lists with city name, state and country.
    """
    api_call = _string_api_call_coordinates(city)
    cities_result = requests.get(api_call) 
    if not cities_result.ok: raise Exception("Error while calling API openweathermap API.")
    cities_info = [[ct["name"], ct["state"] if "state" in ct.keys() else "", ct["country"]] for ct in cities_result.json()]
    return cities_info