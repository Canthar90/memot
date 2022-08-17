from http.client import HTTPException
from locale import currency
from operator import contains
import sys

from urllib.error import HTTPError
import pytest
import requests
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from apis import RandoCatApi, Weather_forecasting, LOTRapi, JokeApi, CurrencyApi


# -----------Testing Cat API-----------------
def test_random_cat():
    """Test if random cat api works correctly"""
    cats = RandoCatApi()
    assert "http" in cats.get_random_cat()


def test_random_cat_not_pased():
    """Test if random cat api gives error after passing there unexpected argument"""
    cats = RandoCatApi()
    with pytest.raises(TypeError):
        cats.get_random_cat("this should not be here")
        

# ------------Testing Weather API------------ 
def test_weather_forecast_pass():
    """Test if checking weather forecasting api works with passed correct parameters"""
    forecasting = Weather_forecasting()
    forecasting.places = {"Torun":  ["53.0137", "18.5981"],}
    assert "Prognoza pogody dla miasta Torun" in forecasting.weather_check()


def test_weather_forecast_fail_argument_passed():
    """Test if weather foracast gives error after passing unexpected argument"""
    forecasting = Weather_forecasting()
    forecasting.places = {"Torun": ["53.0137", "18.5981"],}
    with pytest.raises(TypeError):
        forecasting.weather_check("Beee")
        
        
def test_weather_forecast_fail_nonsence_data():
    """Test if weather forecast returns Http Error 400 with nonsence argument passed """
    forecasting = Weather_forecasting()
    forecasting.places = {"kululumpu": ["231242", "53421"],}
    with pytest.raises(requests.exceptions.HTTPError) as err:
        forecasting.weather_check()
    assert "400" in str(err.value)


def test_weather_foracast_requesting_passed():
    """Test if forecast requesting passes weather for correct place"""
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
def test_currency_api_passes_one_argument():
    """Test if currency api works properly with one argument passed"""
    currency = CurrencyApi()
    response = currency.get_custom("BTC")
    assert type(response) == float


def test_currency_api_passes_two_arguments():
    """Test if currnecy api works with two argument passed"""
    currency = CurrencyApi()
    response = currency.get_custom("BTC", 20)
    assert type(response) == float


def test_currency_api_fails_no_argument_passed():
    """Test if currency api rises exception when no argument is passed"""
    currency = CurrencyApi()
    with pytest.raises(TypeError) as err:
        currency.get_custom()
   

def test_currnecy_api_fails_to_many_arguments_passed():
    """Test if currency api rises exception when to many arguments are passed"""
    currency = CurrencyApi()
    with pytest.raises(TypeError):
        currency.get_custom("BTC", 10, 20, 30)


def test_currency_api_fails_bad_first_argument_str():
    """Test of currency api rises KeyError exception with bad first argument passed
    some random string"""
    currency = CurrencyApi()
    with pytest.raises(KeyError):
        currency.get_custom("Nonsence")


def test_currency_api_fails_bad_first_argument_int():
    """Test if currency api rises KeyError when passed int as a first argument"""
    currency = CurrencyApi()
    with pytest.raises(KeyError):
        currency.get_custom(123123)


def test_currency_api_fails_bad_second_argument_str():
    """Trst if currency api rises KeyError when passed string as a second argument"""
    currency = CurrencyApi()
    with pytest.raises(KeyError):
        currency.get_custom("BTC", "Nonsence")
    