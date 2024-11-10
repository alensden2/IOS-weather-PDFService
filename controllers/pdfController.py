from flask import Blueprint, jsonify, request, current_app
from services.getLatLong import get_lat_long
from services.getWeatherLatLong import get_weather_long_lat

pdf_controller = Blueprint('pdf_controller', __name__)

@pdf_controller.route('/testPDFControllerMain', methods=['GET'])
def test_PDFController():
    current_app.logger.info("City name is missing in the request")
    return jsonify(
        {
            "message": "PDF Controller Works"
        }
    )

@pdf_controller.route('/testPDFController', methods=['GET'])
def getForcastDetails():
    city_name = request.args.get('city')
    if not city_name:
        current_app.logger.error("City name is not present")
        return jsonify({"error" : "city_name is requried"}), 400
    # Get lat and lon 
    current_app.logger.info("fetching city latitude and longitute")
    lon,lat = get_lat_long(cityName=city_name)
    current_app.logger.info("fetching weather with latitude and longitute")
    # get the weather details for upcoming days
    weather_json = get_weather_long_lat(lon, lat)
    # pass lon lat to get full weather json
    return weather_json