import pytest
from activity_suggestions.city import City

def test_city_class():
    with pytest.raises(ValueError):
        wrong_city = City("wrong_city")

    belem = City("Belém")
    goiania = City("Goiânia")
    sao_paulo = City("São Paulo")
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
    belem = City("Belém")
    goiania = City("Goiânia")
    sao_paulo = City("São Paulo")
    assert belem.get_city_weather() in WEATHERS
    assert goiania.get_city_weather() in WEATHERS
    assert sao_paulo.get_city_weather() in WEATHERS

