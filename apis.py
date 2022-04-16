import requests
import datetime
import json



class Weather_forecasting():
    def __init__(self):
        with open("places.json") as file:
            self.places = json.load(file)
        with open("starting.json") as start:
            self.starting = json.load(start)

    def weather_check(self):

        message = ''
        for city in self.places:
            message += self.requesting(city=city)

        return message




    def requesting(self, city):
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
            return (f"Prognoza pogody dla miasta {city}\n"
                        f"Obecna temperatura to: {weather_hourly[0]['temp']}, odczuwalna: {weather_hourly[0]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[0]['pressure']}, widoczność: {weather_hourly[0]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[0]['wind_speed']}km/h, UWAGA PADA DYSZCZ!!!!!! \n"
                        f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h,"
                        f" {weather_hourly[6]['weather'][0]['description']}\n")


        else:
            return (f"Prognoza pogody dla miasta {city}\n"
                        f"Obecna temperatura to: {weather_hourly[0]['temp']}, odczuwalna: {weather_hourly[0]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[0]['pressure']}, widoczność: {weather_hourly[0]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[0]['wind_speed']}km/h, Nie pada,"
                        f" {weather_hourly[0]['weather'][0]['description']} \n"
                        f"Przyszła temperatura to: {weather_hourly[6]['temp']}, odczuwalna: {weather_hourly[6]['feels_like']}, "
                        f"ciśnienie: {weather_hourly[6]['pressure']}, widoczność: {weather_hourly[6]['visibility']}m, "
                        f"prędkość watru: {weather_hourly[6]['wind_speed']}km/h, Nie pada,"
                        f" {weather_hourly[6]['weather'][0]['description']}\n")
