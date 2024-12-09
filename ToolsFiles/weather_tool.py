import os

from dotenv import load_dotenv
import requests


load_dotenv()

api_key = os.getenv("OPENWEATHERMAP_API_KEY")

def get_weather(city_name: str) -> dict | str:
    
    """
    Get the current weather for a given city.

    Args:
        city_name (str): The name of the city to get the weather for.

    Returns:
        dict: A dictionary of the current weather information if the request is successful.
        str: An error message if the request fails.
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()

    else:
        return f"Error: {response.status_code}, {response.text}"