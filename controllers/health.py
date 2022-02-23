from decouple import config as env

from flask import jsonify


def index():
    data = {"message": "Welcome to wordle game {}".format(env("FLASK_ENV"))}
    return jsonify(data), 200
