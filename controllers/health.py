from flask import jsonify


def index():
    data = {"message": "Welcome to wordle game"}
    return jsonify(data), 200
