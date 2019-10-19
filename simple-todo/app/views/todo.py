#!/usr/bin/python3
# View fo To-Do
"""
 Author: Daniel Córdova A.
"""

from app import app
import json
from flask import abort
from flask import request
from flask import jsonify
from ..utils import json_utils

todo_list = ['{"id": 1, "title": "first", "description": "description"}']


@app.route("/", methods=['GET'])
def get_all_todos():
    # Return Json List
    return jsonify(
        [json.loads(each_todo) for each_todo in todo_list]
    )


@app.route("/" + '<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    selected_todo = None
    for element in todo_list:
        if str(json.loads(element)['id']) == todo_id:
            selected_todo = element
    # If Json is None we return a 404 Error code
    if selected_todo is None:
        return abort(404)
    return selected_todo


@app.route("/", methods=['POST'])
def post_todo():
    # Check if request is a valid JSON
    json_utils.is_not_json_request(request)
    id_list = []
    # Iterate To-Do List, take only Id's and add it to a new list
    for element in todo_list:
        id_list.append(json.loads(element)['id'])
    # Order List of id's
    id_list.sort()
    # Add id to Json
    request.json['id'] = id_list[-1] + 1
    # Add json to To-Do list
    todo_list.append(str(json.dumps(request.json)))
    return json.dumps(request.json)


@app.route("/" + '<string:todo_id>', methods=['PUT'])
def put_todo(todo_id):
    return "UPDATED"
