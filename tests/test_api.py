import sys
import pytest
import requests
import os
from unittest.mock import patch

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from apis import RandoCatApi, Weather_forecasting, LOTRapi, JokeApi, CurrencyApi, DrinkApi


# -----------Testing Cat API-----------------
@pytest.mark.cat_api
@patch.object(RandoCatApi, 'get_random_cat')
def test_random_cat(mock_ty_method):
    """Test if random cat api works correctly"""
    mock_ty_method.return_value = "http good cat was picked"
    cats = RandoCatApi()
    assert "http" in cats.get_random_cat()


@pytest.mark.cat_api
def test_random_cat_not_pased():
    """Test if random cat api gives error after passing there unexpected argument"""
    cats = RandoCatApi()
    with pytest.raises(TypeError):
        cats.get_random_cat("this should not be here")
        

# ------------Testing Weather API------------ 
@pytest.mark.weather_api
@patch.object(Weather_forecasting, 'requesting')
def test_weather_forecast_pass(mock_my_method):
    """Test if checking weather forecasting api works with passed correct parameters"""
    mock_my_method.return_value = "Prognoza pogody dla miasta Torun"

    forecasting = Weather_forecasting()
    forecasting.places = {"Torun":  ["53.0137", "18.5981"],}
    assert "Prognoza pogody dla miasta Torun" in forecasting.weather_check()


@pytest.mark.weather_api
def test_weather_forecast_fail_argument_passed():
    """Test if weather foracast gives error after passing unexpected argument"""
    forecasting = Weather_forecasting()
    forecasting.places = {"Torun": ["53.0137", "18.5981"],}
    with pytest.raises(TypeError):
        forecasting.weather_check("Beee")
        

@pytest.mark.weather_api        
def test_weather_forecast_fail_nonsence_data():
    """Test if weather forecast returns Http Error 400 with nonsence argument passed """
    forecasting = Weather_forecasting()
    forecasting.places = {"kululumpu": ["231242", "53421"],}
    with pytest.raises(requests.exceptions.HTTPError) as err:
        forecasting.weather_check()
    assert "400" in str(err.value)


@pytest.mark.weather_api
@patch.object(Weather_forecasting, 'requesting')
def test_weather_foracast_requesting_passed(mock_my_method):
    """Test if forecast requesting passes weather for correct place"""
    mock_my_method.return_value = "Prognoza pogody dla miasta Watykan"

    forecasting = Weather_forecasting()
    forecasting.places = {"Torun": ["53.0137", "18.5981"],
                          "Watykan":  ["41.9024", "12.4533"],  
                          }
    assert "Prognoza pogody dla miasta Watykan" in forecasting.requesting("Watykan")


def test_weather_forecast_requesting_fail_no_city_in_database():
    """Testing if weather forecasting raises TypeError with passed city name that is not 
    in the database"""
    forecasting = Weather_forecasting()
    forecasting.places = {"Torun": ["53.0137", "18.5981"],}
    with pytest.raises(KeyError):
        forecasting.requesting("Korinis")
        

def test_weather_forecast_requesting_fail_multiple_args():
    """Testing if weather forecasting requesting raises exception when more than 1 argument passed"""
    forecasting = Weather_forecasting()
    forecasting.places = {"Torun": ["53.0137", "18.5981"],
                          "Watykan":  ["41.9024", "12.4533"],  
                          }
    with pytest.raises(TypeError) as err: 
        forecasting.requesting("Torun", "Watykan")
    assert "takes 2 positional arguments" in str(err.value)


# ------------------Test LOTR API--------------------------
def test_lotr_api_passes():
    """Test if LOTR api works correctly and gives random LOTR quote by checking it 
    response format"""
    lotr = LOTRapi()
    response = lotr.get_random_quote()
    assert type(response) == str, response


def test_lotr_api_fails_unexpected_arguments():
    """Test if LOTR api raises exception while additional argument passed"""
    lotr = LOTRapi()
    with pytest.raises(TypeError) as err:
        lotr.get_random_quote("random argument")
    assert "takes 1 positional argument" in str(err.value)

    
# --------------- Test Joke API------------------------------
def test_joke_api_passes():
    """Test if joke api works and gives random Joke by checking format of response"""
    jocker = JokeApi()
    response = jocker.get_joke()
    assert type(response) == tuple


def test_joke_api_fails_unexpected_argument():
    """Test if joke api raises exception when called with unexpected argument"""
    jocker = JokeApi()
    with pytest.raises(TypeError) as err:
        jocker.get_joke(5, "oither nonsence")
    assert "takes 1 positional argument" in str(err.value)


# ---------------Test Currency API------------------------
@pytest.mark.currency_test
def test_currency_api_passes_one_argument():
    """Test if currency api works properly with one argument passed"""
    currency = CurrencyApi()
    response, flag = currency.get_custom("BTC")
    try:
        assert type(response) == float and flag == True
    except AssertionError:
        pytest.fail(response)
   

@pytest.mark.currency_test
def test_currency_api_passes_two_arguments():
    """Test if currnecy api works with two argument passed"""
    currency = CurrencyApi()
    response, flag = currency.get_custom("BTC", 20)
    try:
        assert type(response) == float and flag == True
    except AssertionError :
        pytest.fail(response)


@pytest.mark.currency_test
def test_currency_api_fails_no_argument_passed():
    """Test if currency api rises exception when no argument is passed"""
    currency = CurrencyApi()
    with pytest.raises(TypeError) as err:
        currency.get_custom()
   

@pytest.mark.currency_test
def test_currnecy_api_fails_to_many_arguments_passed():
    """Test if currency api rises exception when to many arguments are passed"""
    currency = CurrencyApi()
    with pytest.raises(TypeError):
        currency.get_custom("BTC", 10, 20, 30)


@pytest.mark.currency_test
def test_currency_api_fails_bad_first_argument_str():
    """Test of currency api rises KeyError exception with bad first argument passed
    some random string"""
    currency = CurrencyApi()
    try:
        with pytest.raises(KeyError):
            res, flag = currency.get_custom("Nonsence")
    except:
        pytest.fail(res)
        

@pytest.mark.currency_test
def test_currency_api_fails_bad_first_argument_int():
    """Test if currency api rises KeyError when passed int as a first argument"""
    currency = CurrencyApi()
    try:
        with pytest.raises(KeyError):
            res, flag =currency.get_custom(123123)
    except:
        pytest.fail(res)


@pytest.mark.currency_test
def test_currency_api_fails_bad_second_argument_str():
    """Trst if currency api rises KeyError when passed string as a second argument"""
    currency = CurrencyApi()
    try:
        with pytest.raises(KeyError):
            res, flag = currency.get_custom("BTC", "Nonsence")
    except:
        pytest.fail(res)
        

# -----------------Test Drink API ------------------
def test_random_drink_api_endponit_passes():
    """Test if random drink api endpoint is working"""
    drinks = DrinkApi()
    assert ("Necessary ingredients:" and "Ammount of the ingredients:") in drinks.random_drink() 
    
    
def test_random_drink_api_endpion_fails_argument_fails():
    """Test if random drink api endpiont raises TypeError when any argument passed"""
    drinks = DrinkApi()
    with pytest.raises(TypeError) as err:
       drinks.random_drink("Libre Cuba")
    assert "takes 1 positional argument" in str(err.value)
    

def test_search_by_name_drink_api_endpoint_passes():
    """Test if search drink by name api endpoint is working"""
    drinks = DrinkApi()
    resp = drinks.search_by_name("Cuba Libre")
    assert ("Necessary ingredients:" and "Ammount of the ingredients:") in resp
    
    
def test_search_by_name_drink_api_endpoint_nonsense_argument_fails():
    """Test if search drink by name api endpiont raises TypeError with nonsense
    argument passed"""
    drinks = DrinkApi()
    with pytest.raises(TypeError):    
        drinks.search_by_name("nanskjdhiuwrffq")


def test_search_by_name_drink_api_endpoint_many_arguments_fails():
    """Test if search drink by name api endpoint raises TypeError when
    many argument passed"""
    drinks = DrinkApi()
    with pytest.raises(TypeError) as err:
        drinks.search_by_name("Libre Cuba", "Mojito")
    assert "takes 2 positional arguments" in str(err.value)


def test_search_by_ingredient_drink_api_endpoint_passes():
    """Test if search drink by name api endpoint works fine"""
    drinks = DrinkApi()
    resp_list, resp_flag = drinks.search_by_ingredient("milk")
    assert resp_flag == True and type(resp_list) == list


def test_search_by_ingredient_drink_api_endpoint_false_wrong_arg():
    """Test if search drink by name api endpoint fails when
    invalid argument passed"""
    drinks = DrinkApi()
    resp_mess, resp_flag = drinks.search_by_ingredient("ksajhdkauhs")
    assert resp_flag == False, resp_mess == "You provided bad ingredient name"


def test_search_by_ingredient_drink_api_fails_many_arguments():
    """Test if search drink by name api endpoint rise TypeError
    when many argument passed """
    drinks = DrinkApi()
    with pytest.raises(TypeError) as err:
        drinks.search_by_ingredient("milk", "coffee")
    assert "takes 2 positional arguments" in str(err.value)