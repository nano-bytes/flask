#!/usr/bin/python3
# Application init
"""
 Author: Daniel Córdova A.
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.views import todo
