# Flask imports
from flask import request
from flask_restful import Resource
# JWT imports
from flask_jwt_extended import jwt_required, fresh_jwt_required
from flask_jwt_extended import get_jwt_claims, get_raw_jwt
# @jwt_optional


# 2xx Success
OK = 200
CREATED = 201
ACCEPTED = 202
NO_CONTENT = 204

class Protected(Resource):

    @classmethod
    @fresh_jwt_required
    def get(cls):
        claims = get_jwt_claims()
        return {
            "result": "get", 
            "jwt": "fresh_jwt_required",
            "claims": claims
        }, OK

    @classmethod
    @jwt_required
    def post(cls):
        data = request.get_json()
        claims = get_jwt_claims()
        raw_jwt = get_raw_jwt()
        return {
            "result": "post",
            "data": data,
            "jwt": "jwt_required",
            "claims": claims,
            "raw_jwt": raw_jwt
        }, OK

    @classmethod
    @jwt_required
    def put(cls):
        data = request.get_json()
        return {
            "result": "put",
            "data": data,
            "jwt": "jwt_required"
        }, OK

    @classmethod
    @fresh_jwt_required
    def delete(cls):
        return {
            "result": "delete",
            "jwt": "fresh_jwt_required"
        }, OK
