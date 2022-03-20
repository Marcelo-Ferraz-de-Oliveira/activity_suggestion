import pytest
from activity_suggestions.activities import Activities

UNIQUE_WEATHER = ["Drizze", 
"Clouds", 
"Drizzle", 
"ThunderStorm", 
"Clear", 
"Snow", 
"Rain"]

PARTICIPANTS_NUMBER = [1, 2, 3, 4, 5, 6, 10]

COSTS = ['R$100,00', 
'R$10,00', 
'R$0,00', 
'R$15,00', 
'R$10000,00', 
'R$50,00', 
'R$200,00', 
'R$300,00', 
'R$1000,00', 
'R$30,00']

activities = Activities()

def test_activities_load():
    
    RESULT_ACTIVITIES = {'id': 1, 
    'activity_title': 'Ice skating', 
    'requisites': {'cost': 'R$30,00', 'participants_number': 1}, 
    'suggested_location': 'Ice skating rink', 
    'suggested_weather_conditions': 'Snow', 
    'unsuggested_weather_conditions': []}
    
    assert type(activities.activities) == list
    assert activities.activities[0] == RESULT_ACTIVITIES
    assert sorted(activities.unique_weather) == sorted(UNIQUE_WEATHER)
    assert sorted(activities.participants_number) == sorted(PARTICIPANTS_NUMBER)
    assert sorted(activities.costs) == sorted(COSTS)

def test_activities_filters():
    for weather in UNIQUE_WEATHER:
        for activity in activities.get_activity_by_suggested_weather(weather):
            assert activity['suggested_weather_conditions'] == weather
    for participants_number in PARTICIPANTS_NUMBER:
        for activity in activities.get_activity_by_participants_number(participants_number):
            assert activity['requisites']['participants_number'] == participants_number
    for cost in COSTS:
        for activity in activities.get_activity_by_cost(cost):
            assert activity['requisites']['cost'] == cost

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
