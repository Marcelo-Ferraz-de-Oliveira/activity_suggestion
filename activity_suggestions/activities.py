import requests
import json

class Activities(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self):
        URL_JSON_ACTIVITIES = "https://raw.githubusercontent.com/probono-digital/DesafioTecnico/main/MOCK_DATA.json"
        self.activities = self._get_activities_from_web(URL_JSON_ACTIVITIES)
        self.unique_weather, self.participants_number, self.costs = self._get_unique_weather()
    
    def _get_activities_from_web(self, url):
        activities_request = requests.get(url)
        if not activities_request.ok: raise ValueError(f"Can't get activities form address (error code {activities_request.status_code}) {url}")
        #Convert null prices in R$0,00
        activities = json.loads(activities_request.text.replace("null", "\"R$0,00\""))
        return activities
    
    def add_activity(self, activity):
        activity['id'] = self.activities[-1]['id'] + 1 if self.activities else 1
        self.activities.append(activity)
    
    def get_activity_by_suggested_weather(self, weather):
        #Reload activities
        self.__init__()
        return [activity for activity in self.activities if activity["suggested_weather_conditions"] == weather]

    def get_activity_by_participants_number(self, number):
        self.__init__()
        return [activity for activity in self.activities if activity['requisites']['participants_number'] == number]

    def get_activity_by_participants_number(self, cost):
        self.__init__()
        return [activity for activity in self.activities if activity['requisites']['cost'] == cost]


    def filter_activity_by_unsuggested_weather(self, weather):
        #Reload activities
        self.__init__()
        return [activity for activity in self.activities if weather not in activity["unsuggested_weather_conditions"]]

    def _get_unique_weather(self):
        suggested_weather = [activity["suggested_weather_conditions"] for activity in self.activities]
        participants_numbers = [activity['requisites']['participants_number'] for activity in self.activities]
        costs = [activity['requisites']['cost'] for activity in self.activities]

        return list(set(suggested_weather)), list(set(participants_numbers)), list(set(costs))
