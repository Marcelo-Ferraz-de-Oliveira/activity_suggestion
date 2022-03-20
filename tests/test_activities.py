import pytest
from activity_suggestions.activities import Activities

activities = Activities()

def test_activities_load():
    
    RESULT_ACTIVITIES = {'id': 1, 
    'activity_title': 'Ice skating', 
    'requisites': {'cost': 'R$30,00', 'participants_number': 1}, 
    'suggested_location': 'Ice skating rink', 
    'suggested_weather_conditions': 'Snow', 
    'unsuggested_weather_conditions': []}
    
    RESULT_UNIQUE_WEATHER = ["Drizze", 
    "Clouds", 
    "Drizzle", 
    "ThunderStorm", 
    "Clear", 
    "Snow", 
    "Rain"]

    RESULT_PARTICIPANTS_NUMBER = [1, 2, 3, 4, 5, 6, 10]
    RESULT_COSTS = ['R$100,00', 'R$10,00', 'R$0,00', 'R$15,00', 'R$10000,00', 'R$50,00', 'R$200,00', 'R$300,00', 'R$1000,00', 'R$30,00']

    assert type(activities.activities) == list
    assert activities.activities[0] == RESULT_ACTIVITIES
    assert sorted(activities.unique_weather) == sorted(RESULT_UNIQUE_WEATHER)
    assert sorted(activities.participants_number) == sorted(RESULT_PARTICIPANTS_NUMBER)
    assert sorted(activities.costs) == sorted(RESULT_COSTS)

WEATHER = "Clear"

def test_activities_filters():
    for activity in activities.get_activity_by_suggested_weather(WEATHER):
        assert activity['suggested_weather_conditions'] == WEATHER
    for activity in activities.filter_activity_by_unsuggested_weather(WEATHER):
        assert WEATHER not in activity['unsuggested_weather_conditions']

def test_add_activities():
    ACTIVITY_TO_ADD = {'id': 1, 
    'activity_title': 'Stay in home', 
    'requisites': {'cost': 'R$0,00', 'participants_number': 1}, 
    'suggested_location': 'Home', 
    'suggested_weather_conditions': 'Snow', 
    'unsuggested_weather_conditions': []}
    ACTIVITY_RESULT = {'id': 22, 
    'activity_title': 'Stay in home', 
    'requisites': {'cost': 'R$0,00', 'participants_number': 1}, 
    'suggested_location': 'Home', 
    'suggested_weather_conditions': 'Snow', 
    'unsuggested_weather_conditions': []}

    activities.add_activity(ACTIVITY_TO_ADD)
    assert ACTIVITY_RESULT in activities.activities
