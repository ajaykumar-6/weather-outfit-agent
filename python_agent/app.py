from weather_api import get_weather
from agent_logic import recommend_clothes
from memory import get_user_preferences

def main():
    print("🌦️ Weather-Based Clothing Recommendation Agent")
    city = input("Enter city name: ")

    weather = get_weather(city)
    preferences = get_user_preferences()

    clothes = recommend_clothes(weather, preferences)

    print("\n📍 City:", city)
    print("🌡️ Temperature:", weather["temperature"], "°C")
    print("🌤️ Condition:", weather["condition"])

    print("\n👕 Recommended Clothes:")
    for item in clothes:
        print("-", item)

if __name__ == "__main__":
    main()
