import logging

from flask import jsonify
from flask import request

from util.util import Util


def save():
    decoded_token, status = Util.authorize(request.headers)
    uuid = decoded_token.get('payload_sub')
    request_body = request.get_json()
    if uuid:
        logging.debug(request.method)
        if request.method == 'POST':
            game_obj = {"name": request_body.get("name"), "word_id": request_body.get("word_id")}
            logging.debug(game_obj)
        if request.method == 'PATCH':
            pass
        if request.method == 'DELETE':
            pass
        else:
            data = {"message": "Method not allowed"}
            return jsonify(data), 403
    else:
        return decoded_token
