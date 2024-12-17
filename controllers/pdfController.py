from flask import Blueprint, jsonify, request, current_app
from services.getLatLong import get_lat_long
from services.getWeatherLatLong import get_weather_long_lat
from services.mongoDBCacheCheck import get_weather
import json

pdf_controller = Blueprint('pdf_controller', __name__)

@pdf_controller.route('/testPDFControllerMain', methods=['GET'])
def test_PDFController():
    return jsonify(
        {
            "message": city_name
        }
    )

@pdf_controller.route('/testPDFController', methods=['GET'])
def getForcastDetails():
    city_name = request.args.get('city')
    if not city_name:
        current_app.logger.error("City name is not present")
        return jsonify({"error" : "city_name is requried"}), 400
    # Check cache with city name 
    weather = get_weather(city_name)
    weather_json = json.dumps(weather, default=str)
    return weather_json