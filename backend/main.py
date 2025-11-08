from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS with more explicit settings
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route("/")
def hello():
    return jsonify({"message": "Hello from Flask Backend!"})

if __name__ == "__main__":
    # Make sure to bind to 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', debug=True, port=5001)
