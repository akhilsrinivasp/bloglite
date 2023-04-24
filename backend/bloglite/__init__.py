from flask import Flask
from flask_restful import Api    
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from bloglite.config import LocalDevelopmentConfig
from bloglite.database import db, ma

from bloglite.api import register_api

def create_app(config_class=LocalDevelopmentConfig):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    api = Api(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    JWTManager(app)
    
    api = register_api(api)
    
    with app.app_context():
        db.create_all() 
    return app, api
