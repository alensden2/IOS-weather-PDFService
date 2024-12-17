from flask import Flask, request, jsonify, current_app
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from services.getLatLong import get_lat_long
from services.getWeatherLatLong import get_weather_long_lat
import os
import pymongo

MONGO_URI = os.getenv('MONGO_URI')
client  = MongoClient(MONGO_URI)
db = client['CITY_WEATHER']
COLLECTION =db['WEATHER_CITY']

def get_weather(city):
    try:
        print("weather_data")
        details = COLLECTION.find_one({"City":city})
        if(details):
            print(details)
        else:
            current_app.logger.info("fetching city latitude and longitute")
            lon,lat = get_lat_long(cityName=city)
            current_app.logger.info("fetching weather with latitude and longitute")
            # get the weather details for upcoming days
            weather_json = get_weather_long_lat(lon, lat)
            current_app.logger.info("Adding new city to mongo cache")
            COLLECTION.insert_one({"City" : city, "Weather_Json": weather_json})
            details = COLLECTION.find_one({"City":city})
        # print("City retrieved : ", a)
        return details
    except Exception as e: 
        current_app.logger.error("mongoDBCacheCheck exception in get weather method")
        return jsonify({"error" : str(e)}), 500 