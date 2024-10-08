from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/testPdfService', methods=['GET'])
def testPdfService():
    return jsonify({
        "message" : "PDF service is Online"
    })
if __name__ == '__main__':
    app.run(debug=True)