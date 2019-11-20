#!/usr/bin/python3
# View fo To-Do
"""
 Author: Daniel Córdova A.
"""

from flask import abort, jsonify
from flask import request
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import User
from ..utils import json_utils
from flask_jwt_extended import create_access_token


@app.route("/register", methods=['POST'])
def register():
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    # Extract username from request
    username = request.json.get('username')
    # Search is we have a registered user with provided username
    existent_user = User.query.filter_by(username=username).first()
    # If User exists return a message with 409 conflict code
    if existent_user:
        return jsonify(message="User already exists"), 409
    # If not we will create a new user
    else:
        # Extract password from request
        password = request.json.get('password')
        # Create a new instance of User
        new_user = User(username=username, password=password)
        # Add our new user to a database session
        db.session.add(new_user)
        try:
            # Commit db session -> this will perform "INSERT" operation on db
            db.session.commit()
        except IntegrityError:
            # If something goes wrong it will abort with a 400 error code
            abort(400)
        return jsonify(new_user.json_dump()), 201


@app.route("/login", methods=['POST'])
def login():
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    # Extract data from request
    username = request.json.get('username')
    password = request.json.get('password')
    # Search is we have a registered user with provided username
    logged_user = User.query.filter_by(username=username, password=password).first()
    # Check if provided user exists on database
    if logged_user:
        import datetime
        # Create an identity for our token based on username and current date
        token_identity = "user: {} ~ date: {}".format(username, datetime.datetime.now())
        access_token = create_access_token(identity=token_identity)
        # Return a simple message with the access token
        return jsonify(message="Logged successfully", access_token=access_token), 200
    else:
        # If not exists return a message with 401 Unauthorized code
        return jsonify(message="Bad username or password"), 401
