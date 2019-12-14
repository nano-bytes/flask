#!/usr/bin/python3
# View fo To-Do
"""
 Author: Daniel Córdova A.
 Author: Paul Rodríguez-Ch.
"""

from flask import abort, jsonify
from flask import request
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import User
from ..utils import json_utils, password_utils
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, \
    create_refresh_token, get_jwt_identity, get_raw_jwt, jwt_required

blacklist = set()


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
        # Get hashed password
        hashed_password = password_utils.get_hashed_password_with_sha512(password)
        # Create a new instance of User
        new_user = User(username=username, password=hashed_password)
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
    # Get hashed password
    hashed_password = password_utils.get_hashed_password_with_sha512(password)
    # Search is we have a registered user with provided username
    logged_user = User.query.filter_by(username=username, password=hashed_password).first()
    # Check if provided user exists on database
    if logged_user:
        import datetime
        # Create the data identity for our token based on user_id, username and current date
        user_identity = {
            "user_id": logged_user.id,
            "username": username,
            "date": datetime.datetime.now()
        }
        # Time to token expiration process
        expired_time = datetime.timedelta(minutes=60)
        # Access and Refresh Tokens
        access_token = create_access_token(identity=user_identity, expires_delta=expired_time)
        refresh_token = create_refresh_token(identity=user_identity)
        # Return a simple message with the access token
        return jsonify(access_token=access_token, refresh_token=refresh_token, message="Logged successfully"), 200
    else:
        # If not exists return a message with 401 Unauthorized code
        return jsonify(message="Bad username or password"), 401


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    import datetime
    current_user = get_jwt_identity()
    expired_time = datetime.timedelta(minutes=60)
    new_access_token = create_access_token(identity=current_user, expires_delta=expired_time)
    return jsonify(access_token=new_access_token, message="Token refresh successfully")


# Endpoint for revoking the current users access token
@app.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200


# Endpoint for revoking the current users refresh token
@app.route('/revoke', methods=['DELETE'])
@jwt_refresh_token_required
def logout2():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully revoked"}), 200