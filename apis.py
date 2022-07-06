import requests
import datetime
import json
import random

with open("starting.json") as start:
    starting = json.load(start)


class Weather_forecasting:
    def __init__(self):
        """loading starting data files to dictionaries"""
        with open("places.json") as file:
            self.places = json.load(file)
        with open("starting.json") as start:
            self.starting = json.load(start)

    def weather_check(self):
        """sending all city names from starting file to requesting function"""
        message = ''
        for city in self.places:
            message += self.requesting(city=city)

        return message


    def requesting(self, city):
        """Requesting and forming weather forecast message"""
        WEATHER_API = self.starting['weather_api']
        api_key = self.starting['weather_key']
        parameters = {
            "lat": self.places[city][0],
            "lon": self.places[city][1],
            "exclude": "current,minutely,daily",
            "appid": api_key,
            "units": 'metric',
            "lang": "pl"
        }

        response = requests.get(WEATHER_API, params=parameters)
        response.raise_for_status()
        weather_data = response.json()

        gonna_rain = False
        weather_hourly = weather_data["hourly"]
        weather_future = weather_hourly[:12]
        time = datetime.datetime.now()

        for hour_data in weather_future:
            weather_id = hour_data["weather"][0]["id"]
            if int(weather_id) < 700:
                gonna_rain = True

        if gonna_rain:
            return (f"\nPrognoza pogody dla miasta {city}\n"
                        f"Obecna temperatura to: {weather_hourly[0]['temp']}, odczuwalna: {weather_hourly[0]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[0]['pressure']}, widoczność: {weather_hourly[0]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[0]['wind_speed']}km/h, UWAGA PADA DYSZCZ!!!!!! \n"
                        f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h,"
                        f" {weather_hourly[6]['weather'][0]['description']}\n")


        else:
            return (f"\nPrognoza pogody dla miasta {city}\n"
                        f"Obecna temperatura to: {weather_hourly[0]['temp']}, odczuwalna: {weather_hourly[0]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[0]['pressure']}, widoczność: {weather_hourly[0]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[0]['wind_speed']}km/h, Nie pada,"
                        f" {weather_hourly[0]['weather'][0]['description']} \n"
                        f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h, Nie pada,"
                        f" {weather_hourly[6]['weather'][0]['description']}\n")


class RandoCatApi:
    """API generating random cat image"""
    def __init__(self):
        self.URL = "https://api.thecatapi.com/v1/images/search"

    def get_random_cat(self):
        """Gets random cat api response return message url with kitten"""
        response = requests.get(self.URL)
        self.data = response.json()
        return self.data[0]["url"]


class LOTRapi:
    """Simple lord of the rings api usage"""
    def __init__(self):
        self.Key = starting["lotr_api_key"]
        self.URL = "https://the-one-api.dev/v2"
        self.header = {"Authorization": f"Bearer {self.Key}"}

    def get_random_quote(self):
        """gets random quote from LOTR api"""
        quote_url = self.URL + "/quote"
        response = requests.get(quote_url, headers=self.header)
        quotes = response.json()
        quotes_docked = quotes["docs"]
        random_quote = random.choice(quotes_docked)
        return random_quote["dialog"]


class JokeApi:
    """Joke api to message"""
    def __init__(self):
        self.URL = "https://v2.jokeapi.dev/joke/Any"

    def get_joke(self):
        """Returns simple random joke dictionary with type setup and delivery"""
        response = requests.get(self.URL)
        joke = response.json()
        if joke["type"] == "twopart":
            return joke["setup"], joke["delivery"]
        else:
            return joke["joke"], False


class CurrencyApi:
    """Currency checking api"""
    def __init__(self):
        self.URL = "https://api.apilayer.com/fixer/convert"
        self.API_KEY = starting["currency_api_key"]
        self.header = {
            "apikey": self.API_KEY
        }

    def get_custom(self, currency_name, ammount=1.0):
        """Converts passed currency to PLN"""
        custom_url = self.URL + f"?to=PLN&from={currency_name}&amount={ammount}"
        response = requests.get(custom_url, headers=self.header, data={})
        data = response.json()
        return data["result"]


class DrinkApi:
    """Drink recipe api"""
    def __init__(self):
        self.base_url = "http://www.thecocktaildb.com/api/json/v1/1/"

    def search_by_name(self, drink_name):
        """Searches drink or first of drink list by name"""
        endpoint_url = self.base_url + "search.php?s=" + drink_name
        response = requests.get(endpoint_url)
        return self.response_refactor(response=response)

    def random_drink(self):
        """Give a random drink recipe"""
        endpoint_url = self.base_url + "random.php"
        response = requests.get(endpoint_url)
        return self.response_refactor(response=response)

    def response_refactor(self, response):
        drink = response.json()
        drink = drink["drinks"][0]
        message = ""
        image = drink["strDrinkThumb"].replace("\\", "")
        name = drink["strDrink"]
        ingredients = ""
        measurments = ""
        for key in drink:
            if "strIngredient" in key:
                if drink[key]:
                    ingredients += " " + drink[key] + ";"
            if "strMeasure" in key:
                if drink[key]:
                    measurments += " " + drink[key] + ";"
        message += f"{name} \n" \
                   f"{image} \n Nesesary ingredients: {ingredients} \n Ammount of the ingredients: {measurments}\n" \
                   f"the recipe: {drink['strInstructions']}"
        return message

    def search_by_ingredient(self, ingredient):
        """Searchs how many drinks you can do with given ingredient"""
        endpoint_url = self.base_url + "filter.php?i=" + ingredient
        response = requests.get(endpoint_url)
        try:
            drink_list = response.json()
            drink_list = drink_list["drinks"]
            end_list = []
            for i in range(11):
                end_list.append([drink_list[i]["strDrink"], drink_list[i]["strDrinkThumb"]])
            return end_list, True
        except:
            return ["You provided bad ingredient name"], False
