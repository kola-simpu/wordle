from flask import jsonify
from flask import request

from models.word import Word
from util.util import Util


def save_word():
    decoded_token, status = Util.authorize(request.headers)
    uuid = decoded_token.get('payload_sub')
    request_body = request.get_json()
    if uuid:
        if request.method == 'POST':
            word_obj = {"word": request_body.get("word")}
            word_id = Word.create(word_obj)
            if word_id:
                word_obj.update({"id": word_id})
            return jsonify(word_obj), 200
        if request.method == 'PATCH':
            word_id = request_body.get("id")
            word_obj = {"word": request_body.get("word"), "id": request_body.get("id")}
            Word.update(word_obj)
            word_obj = Word.get(word_id)
            return jsonify(word_obj), 200
        if request.method == 'DELETE':
            word_id = request_body.get("id")
            word_id = Word.delete(word_id)
            return jsonify({"id": word_id}), 204
        else:
            data = {"message": "Method not allowed"}
            return jsonify(data), 403
    else:
        return decoded_token


def get_approved():
    decoded_token, status = Util.authorize(request.headers)
    uuid = decoded_token.get('payload_sub')
    if uuid:
        if request.method == 'POST':
            word_objs = Word.get_all_approved()
            return jsonify(word_objs), 200
        else:
            data = {"message": "Method not allowed"}
            return jsonify(data), 403
    else:
        return decoded_token
