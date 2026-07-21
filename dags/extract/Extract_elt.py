import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class Extract_elt:

    def __init__(self):

        self.API_KEY = os.getenv("API_KEY")

        self.CITIES = [
    # India
    "Chennai", "Bengaluru", "Mumbai", "Delhi", "Hyderabad",
    "Kolkata", "Jaipur", "Lucknow", "Ahmedabad", "Pune","Coimbatore","Tirupathur","Madurai","Vellore","Salem","Tiruchirappalli","Thanjavur","Erode","Nagercoil","Tirunelveli",

    # USA
    "New York", "Los Angeles", "Chicago", "Houston", "Washington",

    # Canada
    "Toronto", "Vancouver", "Ottawa", "Montreal",

    # Europe
    "London", "Paris", "Berlin", "Madrid", "Rome",
    "Amsterdam", "Brussels", "Lisbon", "Munich", "Frankfurt",

    # Asia
    "Tokyo", "Osaka", "Seoul", "Beijing", "Shanghai",
    "Singapore", "Bangkok", "Kuala Lumpur", "Jakarta", "Manila",

    # Middle East
    "Dubai", "Abu Dhabi", "Doha", "Riyadh", "Muscat",

    # Africa
    "Cairo", "Nairobi", "Johannesburg", "Cape Town",

    # Australia
    "Sydney", "Melbourne", "Canberra", "Auckland", "Wellington",

    # South America
    "São Paulo", "Rio de Janeiro", "Buenos Aires", "Mexico City"
]

        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

        self.BRONZE_PATH = r"D:\weather-data\data\bronze"

        os.makedirs(self.BRONZE_PATH, exist_ok=True)

    def extract_weather(self):

        weather_data = []

        ingestion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for city in self.CITIES:

            params = {
                "q": city,
                "appid": self.API_KEY,
                "units": "metric"
            }

            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()

            city_data = response.json()

            city_data["ingestion_time"] = ingestion_time
            city_data["source"] = "OpenWeatherMap"

            weather_data.append(city_data)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"weather_{timestamp}.json"

        local_file = os.path.join(self.BRONZE_PATH, filename)

        with open(local_file, "w", encoding="utf-8") as f:
            json.dump(weather_data, f, indent=4)

        print(f"Created : {local_file}")

        return local_file
    print ("Extracted Successfully")
