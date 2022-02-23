from flask import jsonify
import os

def index():
    data = {"message": "Welcome to wordle game {}".format(os.getenv("FLASK_ENV"))}
    return jsonify(data), 200
