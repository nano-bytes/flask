#!/usr/bin/python3
# Application init
"""
 Author: Daniel Córdova A.
 Author: Paul Rodríguez-Ch.
"""

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# JWT Config
app.config["JWT_SECRET_KEY"] = "my-top-secret-key"
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

jwt = JWTManager(app)

# Token blacklist checker
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


from app.views import todo, user_views
from app.views.user_views import blacklist
