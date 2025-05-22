# OpenWeatherMap.org for weather API.
# Create a free account, go to your account dropdown,
# Click on my API keys.

# Standard unit of measure - Kelvin
# https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API key}

# Metric unit of measure - Celsius
# https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API key}&units=metric

# Imperial unit of measure - Fahrenheit
# https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API key}&units=imperial

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f'\nCurrent Weather for {weather_data["name"]}')

    print(
        f'The temperature is {weather_data["main"]["temp"]} degrees Fahrenheit'
    )

    print(
        f'It feels like {weather_data["main"]["feels_like"]} degrees Fahrenheit and {weather_data["weather"][0]["description"]}.'
    )


if __name__ == "__main__":
    get_current_weather()
