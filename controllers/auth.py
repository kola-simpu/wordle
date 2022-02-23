from flask import jsonify

from util.util import Util


def login(request):
    if request.method == 'POST':
        request_body = request.get_json()
        email = request_body.get('email')
        user = {"id": 1}
        token = Util.encode_auth_token(user)
        data = {'token': token}
        return jsonify(data), 403
