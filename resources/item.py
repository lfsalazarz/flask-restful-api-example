# Flask imports
from flask import request
from flask_restful import Resource

# 2xx Success
OK = 200
CREATED = 201
ACCEPTED = 202
NO_CONTENT = 204
# 3xx Redirection
MOVED_PERMANENTLY = 301
FOUND = 302
NOT_MODIFIED = 304
# 4xx Client Error
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
NOT_ACCEPTABLE = 406
# 5xx Server Error
INTERNAL_SERVER_ERROR = 500
NOT_IMPLEMENTED = 501


class Item(Resource):
    @classmethod
    def get(cls, name: str):
        return {
            "result": "get", 
            "data": name
        }, OK

    @classmethod
    def post(cls, name: str):
        data = request.get_json()
        return {
            "result": "post",
            "data": data
        }, OK

    @classmethod
    def delete(cls, name: str):
        return {
            "result": "delete", 
            "data": name
        }, OK

    @classmethod
    def put(cls, name: str):
        data = request.get_json()
        return {
            "result": "put",
            "data": data
        }, OK


class ItemList(Resource):
    @classmethod
    def get(cls):
        return {"result": []}, OK

    @classmethod
    def post(cls):
        data = request.get_json()
        return {"result": [data]}, OK
