import json

from flask import jsonify


def save(request):
    decoded_token = Auth.authorization(request)
    uuid = decoded_token.get('payload_sub')
    request_body = json.loads(request.body.decode('utf-8'))
    if uuid:
        if request.method == 'POST':
            pass
        if request.method == 'PATCH':
            pass
        if request.method == 'DELETE':
            pass
        else:
            data = {"message": "Method not allowed"}
            return jsonify(data), 403
    else:
        return decoded_token
