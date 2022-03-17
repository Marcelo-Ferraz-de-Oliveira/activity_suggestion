import pytest
from activity_suggestions.city import City, get_cities_list

def test_city_class():
    with pytest.raises(ValueError):
        wrong_city = City("wrong_city", "", "")

    belem = City("Belém","Pará","BR")
    goiania = City("Goiânia","Goiás","BR")
    sao_paulo = City("São Paulo","São Paulo","BR")
    assert belem.lat == -1.45056
    assert goiania.lat == -16.680882
    assert sao_paulo.lat == -23.5506507

def test_city_weather_function():
    WEATHERS = ["Drizze", 
    "Clouds", 
    "Drizzle", 
    "ThunderStorm", 
    "Clear", 
    "Snow", 
    "Rain"]
    belem = City("Belém","Pará","BR")
    goiania = City("Goiânia","Goiás","BR")
    sao_paulo = City("São Paulo","São Paulo","BR")
    assert belem.get_city_weather() in WEATHERS
    assert goiania.get_city_weather() in WEATHERS
    assert sao_paulo.get_city_weather() in WEATHERS

def test_city_get_cities_list():
    #TODO
    list_belem = get_cities_list("Belém")
    EXPECTED_RESULT_BELEM = [['Belém', 'Pará', 'BR'], ['Bethlehem', '', 'PS'], ['Belém', '', 'PT'], ['Belém', 'Alagoas', 'BR'], ['Belém', 'Paraíba', 'BR']]
    assert list_belem == EXPECTED_RESULT_BELEM
    list_goiania = get_cities_list("Goiânia")
    EXPECTED_RESULT_GOIANIA = [['Goiânia', 'Goiás', 'BR'], ['Goiânia', 'Minas Gerais', 'BR'], ['Goiânia', 'Minas Gerais', 'BR'], ['Vila Goiânia', 'Rio Grande do Sul', 'BR'], ['Goiânia', 'Espírito Santo', 'BR']]    
    assert list_goiania == EXPECTED_RESULT_GOIANIA
    list_sao_paulo = get_cities_list("São Paulo")
    EXPECTED_RESULT_SAO_PAULO = [['São Paulo', 'São Paulo', 'BR'], ['São Paulo', 'Luanda Province', 'AO'], ['São Paulo', 'Bahia', 'BR'], ['São Paulo', 'Bahia', 'BR'], ['São Paulo', 'Rio Grande do Sul', 'BR']]
    assert list_sao_paulo == EXPECTED_RESULT_SAO_PAULO
    with pytest.raises(ValueError):
        list_wrong_name = get_cities_list("wrong name")


