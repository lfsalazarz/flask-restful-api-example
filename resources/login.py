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
# HTTP Status Codes
from config.constants import OK, UNAUTHORIZED
# Schemas imports
from schemas.login import LoginSchema
from config.decorators import validation


class Login(Resource):
    @classmethod
    @validation
    def post(cls):
        data = request.get_json()
        if not data:
            return {
                "message": "Invalid credentials"
            }, UNAUTHORIZED
        # id = data.get('id', None)
        data = LoginSchema(**data)
        access_token = create_access_token(identity=data.id, fresh=True)
        refresh_token = create_refresh_token(data.id)
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
