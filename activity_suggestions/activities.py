import requests

class Activities(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self):
        URL_JSON_ACTIVITIES = "https://raw.githubusercontent.com/probono-digital/DesafioTecnico/main/MOCK_DATA.json"
        self.activities = self._get_activities_from_web(URL_JSON_ACTIVITIES)
        self.unique_weather = self._get_unique_weather()
    
    def _get_activities_from_web(self, url):
        activities_request = requests.get(url)
        if not activities_request.ok: raise ValueError(f"Can't get activities form address (error code {activities_request.status_code}) {url}")
        return activities_request.json()
    
    def add_activity(self, activity):
        activity['id'] = self.activities[-1]['id'] + 1 if self.activities else 1
        self.activities.append(activity)
    
    def get_activity_by_suggested_weather(self, weather):
        return [activity for activity in self.activities if activity["suggested_weather_conditions"] == weather]

    def filter_activity_by_unsuggested_weather(self, weather):
        return [activity for activity in self.activities if weather not in activity["unsuggested_weather_conditions"]]

    def _get_unique_weather(self):
        suggested_weather = [activity["suggested_weather_conditions"] for activity in self.activities]
        return list(set(suggested_weather))
