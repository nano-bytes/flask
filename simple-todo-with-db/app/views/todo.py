#!/usr/bin/python3
# View fo To-Do
"""
 Author: Daniel Córdova A.
"""

import json

from flask import abort, jsonify
from flask import request
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models import ToDo
from ..utils import json_utils


@app.route("/", methods=['GET'])
def get_all_todos():
    # Query all ToDos in database
    all_todos = ToDo.query.all()
    # Return Json List
    return jsonify([each_todo.json_dump() for each_todo in all_todos])


@app.route("/" + '<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    # Query a To-Do by its ID
    selected_todo = ToDo.query.get(todo_id)
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        abort(404)
    return jsonify(selected_todo.json_dump())


@app.route("/", methods=['POST'])
def post_todo():
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    try:
        # Extract data from request
        title = request.json.get('title')
        description = request.json.get('description')
        # Create an instance of a new To-Do
        new_todo = ToDo(title=title, description=description)
        # Add To-Do to db session
        db.session.add(new_todo)
        # Commit db session -> this will perform "INSERT" operation on db
        db.session.commit()
    except IntegrityError:
        # If something goes wrong it will abort with a 400 error code
        abort(400)
    return jsonify(request.json)


@app.route("/" + '<string:todo_id>', methods=['PUT'])
def put_todo(todo_id):
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    # Query a To-Do by its ID
    selected_todo = ToDo.query.get(todo_id)
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        abort(404)
    # Extract data from request
    selected_todo.title = request.json.get('title')
    selected_todo.description = request.json.get('description')
    try:
        # Commit db session -> this will perform "DELETE" operation on db
        db.session.commit()
    except IntegrityError:
        # If something goes wrong it will abort with a 400 error code
        abort(400)
    return json.dumps(request.json)


@app.route("/" + '<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    # Query a To-Do by its ID
    selected_todo = ToDo.query.get(todo_id)
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        abort(404)
    # Delete To-Do from db session
    db.session.delete(selected_todo)
    try:
        # Commit db session -> this will perform "DELETE" operation on db
        db.session.commit()
    except IntegrityError:
        # If something goes wrong it will abort with a 400 error code
        abort(400)
    return ""
