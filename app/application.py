from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

# Error handler to return JSON for HTTPExceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = jsonify(message=e.description)
    response.status_code = e.code
    return response

# Import routes to register endpoints
from app.routes import books, users, reservation

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)
