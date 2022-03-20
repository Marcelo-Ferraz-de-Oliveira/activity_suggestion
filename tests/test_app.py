import pytest
from activity_suggestions.app import create_app

WEATHER = ["Drizze", 
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

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_city(client):
    response_manaus = client.post("/citieslist", data={
        "city":"Manaus"
    }).json
    EXPECTED_RESULT_MANAUS = [['Manaus', 'Amazonas', 'BR'], ['Manaus', 'Amazonas', 'BR'], ['Manaus', 'Maranhão', 'BR'], ['Manaus', 'Acre', 'BR'], ['Manaus', 'Acre', 'BR']]
    assert response_manaus == EXPECTED_RESULT_MANAUS
    
    response_belem = client.post("/citieslist", data={
        "city":"Belem"
    }).json
    EXPECTED_RESULT_BELEM = [['Bethlehem', '', 'PS'], ['Belém', 'Pará', 'BR'], ['Belém', '', 'PT'], ['Belém', 'Alagoas', 'BR'], ['Belém', 'Paraíba', 'BR']]
    assert response_belem == EXPECTED_RESULT_BELEM
    
    response_sao_paulo = client.post("/citieslist", data={
        "city":"São Paulo"
    }).json
    EXPECTED_RESULT_SAO_PAULO = [['São Paulo', 'São Paulo', 'BR'], ['São Paulo', 'Luanda Province', 'AO'], ['São Paulo', 'Bahia', 'BR'], ['São Paulo', 'Bahia', 'BR'], ['São Paulo', 'Rio Grande do Sul', 'BR']]
    assert response_sao_paulo == EXPECTED_RESULT_SAO_PAULO
    
    response_wrong_city = client.post("/citieslist", data={
        "city":"wrong city name"
    }).json
    EXPECTED_RESULT_WRONG_CITY = []
    assert response_wrong_city == EXPECTED_RESULT_WRONG_CITY

def test_activities_unique_values(client):


    EXPECTED_RESPONSE =  {"activities_weather": sorted(WEATHER),
            "activities_participants_number": sorted(PARTICIPANTS_NUMBER), 
            "activities_costs":sorted(COSTS)}
    
    response = client.post("/getactivitiesuiniquevalues").json
    assert EXPECTED_RESPONSE == response


def test_get_activities_by_city(client):
    #Because weather may change, this test will only verify the returned keys
    EXPECTED_RESULT = ["city","weather","activities"]
    
    response_manaus = client.post("/getactivitiesbycity", data={
        "city":"Manaus", "state": "Amazonas", "country": "BR"
    }).json.keys()
    assert list(response_manaus) == EXPECTED_RESULT    
    
    response_belem = client.post("/getactivitiesbycity", data={
        "city":"Belém", "state": "Pará", "country": "BR"
    }).json.keys()
    assert list(response_belem) == EXPECTED_RESULT    
    
    response_sao_paulo = client.post("/getactivitiesbycity", data={
        "city":"São Paulo", "state": "São Paulo", "country": "BR"
    }).json.keys()
    assert list(response_sao_paulo) == EXPECTED_RESULT

    EXPECTED_RESULT_WRONG_CITY = None
    response_wrong_city = client.post("/getactivitiesbycity", data={
        "city":"wrong city name", "state":"wrong state name", "country": "also wrong"
    }).json
    assert response_wrong_city == EXPECTED_RESULT_WRONG_CITY

def test_activities_by_weather(client):
    for weather in WEATHER:
        activities = client.post("/getactivitiesbyweather", data={"weather":weather }).json
        for activity in activities["activities"]:
            assert activity["suggested_weather_conditions"] == weather
    
    assert {"activities": []} == client.post("/getactivitiesbyweather", data={"weather":"wrong_weather" }).json

def test_activities_by_participants_number(client):
    for participants_number in PARTICIPANTS_NUMBER:
        activities = client.post("/getactivitiesbyparticipantsnumber", data={"participants_number":participants_number }).json
        for activity in activities["activities"]:
            assert activity["requisites"]["participants_number"] == participants_number
    
    assert {"activities": []} == client.post("/getactivitiesbyparticipantsnumber", data={"participants_number":99999999999999999999999 }).json

def test_activities_by_cost(client):
    for cost in COSTS:
        activities = client.post("/getactivitiesbycost", data={"cost":cost }).json
        for activity in activities["activities"]:
            assert activity["requisites"]["cost"] == cost

    assert {"activities": []} == client.post("/getactivitiesbycost", data={"cost":"wrong_cost" }).json

