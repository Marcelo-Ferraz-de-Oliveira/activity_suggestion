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
    EXPECTED_RESULT_WRONG_CITY = "Cidade não encontrada."
    assert response_wrong_city == EXPECTED_RESULT_WRONG_CITY

def test_activities():
    pass
