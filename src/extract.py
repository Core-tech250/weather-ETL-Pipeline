import requests
from config import API_URL

def fetch_weather():
    """Extract weather data from Open-Meteo API"""
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()   
    return response.json()