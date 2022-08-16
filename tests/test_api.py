
from http.client import HTTPException
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

from apis import RandoCatApi, Weather_forecasting


def test_random_cat():
    """Test if random cat api works correctly"""
    cats = RandoCatApi()
    assert "http" in cats.get_random_cat()


def test_random_cat_not_pased():
    """Test if random cat api gives error after passing there unexpected argument"""
    cats = RandoCatApi()
    with pytest.raises(TypeError):
        cats.get_random_cat("this should not be here")
        
        
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
    """Test if weather forecast """
    forecasting = Weather_forecasting()
    forecasting.places = {"kululumpu": ["231242", "53421"],}
    with pytest.raises(requests.exceptions.HTTPError):
        forecasting.weather_check()

        
    