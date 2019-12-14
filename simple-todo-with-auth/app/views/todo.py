#!/usr/bin/python3
# View fo To-Do
"""
 Author: Daniel Córdova A.
 Author: Paul Rodríguez-Ch.
"""

import json

from flask import abort, jsonify
from flask import request
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models import ToDo
from ..utils import json_utils
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route("/", methods=['GET'])
@jwt_required
def get_all_todos():
    # Current user from access token
    current_user_id = get_jwt_identity()['user_id']
    # Query all ToDos in database
    all_todos = ToDo.query.filter_by(user_id=current_user_id)
    # Return Json List
    return jsonify([each_todo.json_dump() for each_todo in all_todos])


@app.route("/" + '<string:todo_id>', methods=['GET'])
@jwt_required
def get_todo(todo_id):
    # Current user from access token
    current_user_id = get_jwt_identity()['user_id']
    # Query a To-Do by its ID
    selected_todo = ToDo.query.filter_by(id=todo_id, user_id=current_user_id)
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        return jsonify(message="Item not found"), 404
    return jsonify(selected_todo.json_dump())


@app.route("/", methods=['POST'])
@jwt_required
def post_todo():
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    try:
        # Current user from access token
        current_user_id = get_jwt_identity()['user_id']
        # Extract data from request
        title = request.json.get('title')
        description = request.json.get('description')
        # Create an instance of a new To-Do
        new_todo = ToDo(user_id=current_user_id, title=title, description=description)
        # Add To-Do to db session
        db.session.add(new_todo)
        # Commit db session -> this will perform "INSERT" operation on db
        db.session.commit()
    except IntegrityError:
        # If something goes wrong it will abort with a 400 error code
        abort(400)
    return jsonify(request.json), 201


@app.route("/" + '<string:todo_id>', methods=['PUT'])
@jwt_required
def put_todo(todo_id):
    # Current user from access token
    current_user_id = get_jwt_identity()['user_id']
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    # Query a To-Do by its ID
    selected_todo = ToDo.query.filter_by(id=todo_id, user_id=current_user_id).first()
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        return jsonify(message="Item not found"), 404
    # Extract data from request
    selected_todo.title = request.json.get('title')
    selected_todo.description = request.json.get('description')
    try:
        # Commit db session
        db.session.commit()
    except IntegrityError:
        # If something goes wrong it will abort with a 400 error code
        abort(400)
    return json.dumps(request.json)


@app.route("/" + '<string:todo_id>', methods=['DELETE'])
@jwt_required
def delete_todo(todo_id):
    # Current user from access token
    current_user_id = get_jwt_identity()['user_id']
    # Query a To-Do by its ID
    selected_todo = ToDo.query.filter_by(id=todo_id, user_id=current_user_id)
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        return jsonify(message="Item not found"), 404
    # Delete To-Do from db session
    db.session.delete(selected_todo)
    try:
        # Commit db session -> this will perform "DELETE" operation on db
        db.session.commit()
    except IntegrityError:
        # If something goes wrong it will abort with a 400 error code
        abort(400)
    return ""
