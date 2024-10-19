from flask import Flask, request, jsonify
from controllers.pdfController import pdf_controller
import logging

app = Flask(__name__)

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
    app.run(debug=True)