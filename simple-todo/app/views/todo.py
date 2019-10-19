#!/usr/bin/python3
# View fo To-Do
"""
 Author: Daniel Córdova A.
"""

from app import app


@app.route("/", methods=['GET'])
def get_all_todos():
    return "TODO's"


@app.route("/"+'<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    return "TODO"


@app.route("/", methods=['POST'])
def post_todo():
    return "POSTED"


@app.route("/"+'<int:todo_id>', methods=['PUT'])
def put_todo(todo_id):
    return "UPDATED"