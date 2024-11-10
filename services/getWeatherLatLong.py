import requests
import os
import json
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request, current_app

load_dotenv()

with open('constants.json') as f:
    config = json.load(f)

API_KEY = os.getenv('OPEN_WEATHER_API')

def get_weather_long_lat(lat, lon):
    lat_str = str(lat)
    lon_str = str(lon)
    url = f"https://api.openweathermap.org/data/2.5/forecast?units=metric&appid={API_KEY}&lat={lat}&lon={lon}"
    print(url)
    current_app.logger.info("Requesting weather from Lat Long from")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        current_app.logger.info("Response code from fetch weather with lat lon {response.raise_for_status}")
        if response.status_code==200:
            current_app.logger.info("Response 200 ... Fetched weather with Long Lat")
            loaded_response = response.json()
            clean_response = loaded_response['list']
            return clean_response
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
   
    
