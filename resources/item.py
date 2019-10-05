# Flask imports
from flask import request
from flask_restful import Resource

from config.constants import OK

class Item(Resource):
    @classmethod
    def get(cls, name: str):
        return {
            "method": "get", 
            "data": name
        }, OK

    @classmethod
    def post(cls, name: str):
        data = request.get_json()
        return {
            "method": "post",
            "data": data
        }, OK

    @classmethod
    def delete(cls, name: str):
        return {
            "method": "delete", 
            "data": name
        }, OK

    @classmethod
    def put(cls, name: str):
        data = request.get_json()
        return {
            "method": "put",
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
