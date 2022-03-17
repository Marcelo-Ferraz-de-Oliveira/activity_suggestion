import pytest
from activity_suggestions.app import create_app

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

def test_home(client):
    response = client.get("/").data.decode()
    EXPECTED_STRING = "You need to enable JavaScript to run this app."
    assert EXPECTED_STRING in response

def test_city(client):
    response_manaus = client.post("/city", data={
        "city":"Manaus"
    }).json
    EXPECTED_RESULT_MANAUS = [['Manaus', 'Amazonas', 'BR'], ['Manaus', 'Amazonas', 'BR'], ['Manaus', 'Maranhão', 'BR'], ['Manaus', 'Acre', 'BR'], ['Manaus', 'Acre', 'BR']]
    assert response_manaus == EXPECTED_RESULT_MANAUS
    
    response_belem = client.post("/city", data={
        "city":"Belem"
    }).json
    EXPECTED_RESULT_BELEM = [['Bethlehem', '', 'PS'], ['Belém', 'Pará', 'BR'], ['Belém', '', 'PT'], ['Belém', 'Alagoas', 'BR'], ['Belém', 'Paraíba', 'BR']]
    assert response_belem == EXPECTED_RESULT_BELEM
    
    response_sao_paulo = client.post("/city", data={
        "city":"São Paulo"
    }).json
    EXPECTED_RESULT_SAO_PAULO = [['São Paulo', 'São Paulo', 'BR'], ['São Paulo', 'Luanda Province', 'AO'], ['São Paulo', 'Bahia', 'BR'], ['São Paulo', 'Bahia', 'BR'], ['São Paulo', 'Rio Grande do Sul', 'BR']]
    assert response_sao_paulo == EXPECTED_RESULT_SAO_PAULO
    
    response_wrong_city = client.post("/city", data={
        "city":"wrong city name"
    }).data.decode()
    EXPECTED_RESULT_WRONG_CITY = "City not found."
    assert response_wrong_city == EXPECTED_RESULT_WRONG_CITY

def test_activities(client):
    #Because weather may change, this test will only verify the returned keys
    EXPECTED_RESULT = ["city","weather","activities"]
    
    response_manaus = client.post("/activities", data={
        "city":"Manaus", "state": "Amazonas", "country": "BR"
    }).json.keys()
    assert list(response_manaus) == EXPECTED_RESULT    
    
    response_belem = client.post("/activities", data={
        "city":"Belém", "state": "Pará", "country": "BR"
    }).json.keys()
    assert list(response_belem) == EXPECTED_RESULT    
    
    response_sao_paulo = client.post("/activities", data={
        "city":"São Paulo", "state": "São Paulo", "country": "BR"
    }).json.keys()
    assert list(response_sao_paulo) == EXPECTED_RESULT

    EXPECTED_RESULT_WRONG_CITY = "City not found."
    response_wrong_city = client.post("/activities", data={
        "city":"wrong city name", "state":"wrong state name", "country": "also wrong"
    }).data.decode()
    assert response_wrong_city == EXPECTED_RESULT_WRONG_CITY
