from flask import Flask, request, jsonify
from controllers.pdfController import pdf_controller
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='w'
)

@app.route('/testPdfService', methods=['GET'])
def testPdfService():
    return jsonify({
        "message" : "PDF service is Online"
    })

app.register_blueprint(pdf_controller)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)