# Standard library imports
import os

# Flask imports
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Resources imports
from resources.item import Item, ItemList
from resources.login import Login, TokenRefresh
from resources.protected import Protected

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
# https://flask-jwt-extended.readthedocs.io/en/latest/options.html
app.secret_key = os.environ.get("APP_SECRET_KEY")
app.config['JWT_ALGORITHM'] = 'RS256' # https://pyjwt.readthedocs.io/en/latest/algorithms.html
app.config['JWT_PUBLIC_KEY'] = open('./certs/localhost.crt').read()
app.config['JWT_PRIVATE_KEY'] = open('./certs/localhost.key').read()
api = Api(app)

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    return {"user_claims_loader": "value"}

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "message": "Signature verification failed.",
        "error": "invalid_token"
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        "error": "authorization_required"
    }), 401

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Login, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(Protected, '/protected')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
