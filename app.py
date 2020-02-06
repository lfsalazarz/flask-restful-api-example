# Standard library imports
import os

# Flask imports
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from dotenv import load_dotenv

# Resources imports
from resources.item import Item, ItemList
from resources.login import Login, TokenRefresh
from resources.protected import Protected
# HTTP Status Codes
from config.constants import UNAUTHORIZED

load_dotenv(".env")

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
# https://flask-jwt-extended.readthedocs.io/en/latest/options.html
app.secret_key = os.environ.get('APP_SECRET_KEY')
app.config['JWT_ALGORITHM'] = 'RS256' # https://pyjwt.readthedocs.io/en/latest/algorithms.html
app.config['JWT_PUBLIC_KEY'] = open('./certs/pubkey.pem').read()
app.config['JWT_PRIVATE_KEY'] = open('./certs/localhost.key').read()
api = Api(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
jwt = JWTManager(app)


# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#   return response

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    return {"user_claims_loader": "value"}

# https://flask-jwt-extended.readthedocs.io/en/latest/changing_default_behavior.html#changing-callback-functions
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "message": "Signature verification failed.",
        "error": "invalid_token"
    }), UNAUTHORIZED

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        "error": "authorization_required"
    }), UNAUTHORIZED

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), UNAUTHORIZED

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        "description": "The token is not fresh.",
        'error': 'fresh_token_required'
    }), UNAUTHORIZED

# @jwt.revoked_token_loader
# @jwt.token_in_blacklist_loader

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Login, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(Protected, '/protected')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
