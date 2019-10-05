# Flask imports
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity
    # jwt_required,
    # get_raw_jwt, # this will return the python dictionary which has all of the claims of the JWT 
)


# 2xx Success
OK = 200
CREATED = 201
ACCEPTED = 202
NO_CONTENT = 204
# 4xx Client Error
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
NOT_ACCEPTABLE = 406


class Login(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        if not data:
            return {
                "message": "Invalid credentials"
            }, UNAUTHORIZED
        id = data.get('id', None)
        access_token = create_access_token(identity=id, fresh=True)
        refresh_token = create_refresh_token(id)
        return ({
            "access_token": access_token, 
            "refresh_token": refresh_token
        }, OK)


class TokenRefresh(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, OK
