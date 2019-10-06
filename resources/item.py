# Flask imports
from flask import request
from flask_restful import Resource

# Schemas imports
from schemas.item import ItemSchema
from json import loads
from pydantic import ValidationError
from config.decorators import validation

from config.constants import OK, BAD_REQUEST


class Item(Resource):
    @classmethod
    def get(cls, name: str):
        return {
            "method": "get", 
            "data": name
        }, OK

    @classmethod
    @validation
    def post(cls, name: str):
        data = request.get_json()
        data = ItemSchema(**data)
        return {
            "method": "post",
            "data": loads(data.json())
        }, OK
        

    @classmethod
    def delete(cls, name: str):
        return {
            "method": "delete", 
            "data": name
        }, OK

    @classmethod
    def put(cls, name: str):
        try:
            data = request.get_json()
            data = ItemSchema(**data)
            return {
                "method": "put",
                "data": loads(data.json())
            }, OK
        except ValidationError as e:
            return {"err": loads(e.json())}, BAD_REQUEST


class ItemList(Resource):
    @classmethod
    def get(cls):
        return {"result": []}, OK

    @classmethod
    def post(cls):
        data = request.get_json()
        return {"result": [data]}, OK
