import requests
import os 
import json
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request, current_app

load_dotenv()

with open('constants.json') as f:
    config = json.load(f)

API_KEY = os.getenv('OPEN_WEATHER_API')

# get lat and long based on city name 
def get_lat_long(cityName):
    url = f"{config['OPEN_WEATHERMAP_DOMAIN']}"+"/"+f"{config['OPEN_WEATHERMAP_CITY_CLIMATE']}"+"&"+"appid="+API_KEY+"&"+"q="+cityName
    current_app.logger.info("Requesting for Lat Long from")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if response.status_code==200:
            loaded_response = response.json()
            current_app.logger.info("Response 200 ... Fetched Long Lat")
            lon = loaded_response['coord']['lon']
            lat = loaded_response['coord']['lat']
            return lon,lat
    except requests.exceptions.HTTPError as http_err:
            # Log the HTTP error
            current_app.logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Log any other request-related errors
        current_app.logger.error(f"Request error occurred: {req_err}")
    except Exception as err:
        # Log any other unexpected errors
        current_app.logger.error(f"An unexpected error occurred: {err}")
    return None