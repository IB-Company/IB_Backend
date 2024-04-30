import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherService:

    def __init__(self):
        self.api_key = os.getenv('WEATHER_KEY')

    async def get_weather_data(self):
        lat = 35.18869937160062
        lon = 128.90341247360877
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}'
        )
        response = json.loads(response.text)
        if response['cod'] != 200:
            return response['message']

        weather = response["weather"][0]["main"]
        data = {
            "lon": response["coord"]["lon"],
            "lat": response["coord"]["lat"],
            "weather": weather,
            "weather_description": response["weather"][0]["description"],
            "temperature": (response['main']['temp'] - 32) * 9 / 5,
            "perceived_temperature": (response['main']['feels_like'] - 32) * 9 / 5,
            "max_temperature": (response['main']['temp_min'] - 32) * 9 / 5,
            "min_temperature": (response['main']['temp_max'] - 32) * 9 / 5,
            "humidity": response['main']['humidity'],
            "visibility": response['visibility'],
            "wind_speed": response['wind']['speed'],
            "wind_deg": response['wind']['deg'],
            "time": response['dt']
        }

        if weather == "Clouds":
            data["cloudiness"] = f"{response['clouds']['all']}%"
        elif weather == "Rain":
            data["rain_1h"] = f"{response['rain']['rain.1h']}mm"
            data["rain_3h"] = f"{response['rain']['rain.1h']}mm"
        elif weather == "Snow":
            data["snow_1h"] = f"{response['snow']['snow.1h']}mm"
            data["snow_3h"] = f"{response['snow']['snow.3h']}mm"

        return data
