#!/usr/bin/python3
# Configuration for the Service
"""
 Author: Daniel Córdova A.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # This configuration allows us to create a SQLite DB with name "to-do.db" inside our project folder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'to-do.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
