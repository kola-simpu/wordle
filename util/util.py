import datetime
import os

import jwt


class Util:
    def authorize(request):
        authorization = request.META.get('HTTP_AUTHORIZATION')
        if authorization:
            decoded_token = Util.decode_auth_token(authorization)
            return decoded_token
        else:
            return {'message': 'Not allowed! Please send a valid Authorization key in header'}, 401

    @staticmethod
    def encode_auth_token(user):
        '''
        Generates the Auth Token
        :return: string
        '''
        try:
            sub = user.get('id')
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': sub
            }
            return jwt.encode(payload, os.getenv('JWT_TOKEN'), algorithm='HS256').decode('utf-8')
        except Exception as e:
            return {'message': 'Internal server error'}, 505

    @staticmethod
    def decode_auth_token(auth_token):
        '''
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        '''
        try:
            payload = jwt.decode(auth_token, os.getenv('JWT_TOKEN'))
            return {'payload_sub': payload['sub']}, 200
        except jwt.ExpiredSignatureError:
            return {'message': 'Expired token'}, 410
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token'}, 401
