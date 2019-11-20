#!/usr/bin/python3
# Application init
"""
 Author: Daniel Córdova A.
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
jwt = JWTManager(app)

# JWT Config
app.config["JWT_SECRET_KEY"] = "my-top-secret-key"

from app.views import todo, user_views
