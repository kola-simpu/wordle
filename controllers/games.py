from flask import jsonify
from flask import request

from models.game import Game
from util.util import Util


def save_game():
    decoded_token, status = Util.authorize(request.headers)
    uuid = decoded_token.get('payload_sub')
    request_body = request.get_json()
    if uuid:
        if request.method == 'POST':
            game_obj = {"name": request_body.get("name"), "word_id": request_body.get("word_id")}
            game_id = Game.create(game_obj)
            if game_id:
                game_obj.update({"id": game_id})
            return jsonify(game_obj), 200
        if request.method == 'PATCH':
            pass
        if request.method == 'DELETE':
            pass
        else:
            data = {"message": "Method not allowed"}
            return jsonify(data), 403
    else:
        return decoded_token
