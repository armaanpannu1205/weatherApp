import requests
from datetime import datetime

# Constants
WEATHER_API_KEY = "991f0f0d94cc1154dcb2fd8a7f89c27a"
WEATHER_API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data for a location
def get_weather_data(location):
    url = f"{WEATHER_API_BASE_URL}?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") == "404":
        return None
    weather = {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }
    return weather

# Function to display weather data
def display_weather_data(location, weather_data):
    if weather_data is None:
        print(f"Weather data for {location} isn't available.")
    else:
        print(f"\nWeather in {location}:")
        print("Temperature:", weather_data["temperature"], "°C")
        print("Description:", weather_data["description"])
        print("Humidity:", weather_data["humidity"], "%")
        print("Wind Speed:", weather_data["wind_speed"], "m/s")

# Function to get season based on the current month
def get_season():
    current_month = datetime.now().month
    if 3 <= current_month <= 5:
        return "spring"
    elif 6 <= current_month <= 8:
        return "summer"
    elif 9 <= current_month <= 11:
        return "autumn"
    else:
        return "winter"

# Function to recommend vacation spots based on the season
def recommend_vacation_spot():
    print("Welcome to the Vacation Spot Recommender!")
    favorites = []
    while True:
        location = input("Enter the name of a location to get weather data (or type 'exit' to quit): ").strip()
        if location.lower() == "exit":
            print(f"\nYour favorites list is: {favorites}")
            break
        weather_data = get_weather_data(location)
        display_weather_data(location, weather_data)
        season = get_season()
        print(f"Considering the current season ({season}), here are some recommendations:")
        if season == "spring":
            print("- Flower festivals in Kyoto, Japan")
            print("- Cherry blossoms in Washington, D.C.")
        elif season == "summer":
            print("- Beach vacation in Bali, Indonesia")
            print("- Surfing in Honolulu, Hawaii")
        elif season == "autumn":
            print("- Fall foliage in Vermont, USA")
            print("- Wine tasting in Tuscany, Italy")
        else:
            print("- Skiing in Aspen, Colorado")
            print("- Northern Lights in Tromsø, Norway")

        add_favorite = input("Would you like to add this location to your favorites list? (y/n): ").strip().lower()
        if add_favorite == "y":
            favorites.append(location)
            print(f"{location} has been added to your favorites list!")
    print("Thanks for using the Vacation Spot Recommender!")

# Run the vacation spot recommender
recommend_vacation_spot()
