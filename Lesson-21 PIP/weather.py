import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()


def get_current_weather():
    print("\n** Get current Weather COnditions ***\n")
    city = input("\nPlease enter a city name:\n")

    request_url = (
        f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"
    )

    #print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f"\nCurrent weather for {weather_data['name']}\n")
    print(f"\nThe Temp is {weather_data['main']['temp']}\n")
    print(f"\nFeels like {weather_data['main']['feels_like']} and {weather_data["weather"][0]["description"]}\n")


if __name__ == "__main__":
   get_current_weather()
