import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    city = city.split(",")[0].strip()

    if not API_KEY:
        raise Exception("OpenWeather API key not found")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data.get("message", "Failed to fetch weather"))

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }


    return weather_data
