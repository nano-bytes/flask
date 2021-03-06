#!/usr/bin/python3
# Models for Series MicroService
"""
 Author: Daniel Córdova A.
 Author: Paul Rodríguez-Ch.
"""

from app import db
from uuid import uuid4


# This class contains the model that will create a table for users inside our Database
class User(db.Model):
    # Id is a integer and is the primary key
    id = db.Column(db.Integer, primary_key=True, default=lambda: uuid4().hex)
    # Username is a text value and also is primary key
    username = db.Column(db.Text, primary_key=True)
    # Password is a text value and not allowed to be empty
    password = db.Column(db.Text, nullable=False)

    def json_dump(self):
        return dict(
            id=self.id,
            username=self.username
        )

    def __repr__(self):
        return '<User Name%r>' % self.username


# This class contains the model that will create a table for To-Do's inside our Database
class ToDo(db.Model):
    # Id is a integer and is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # User id is a integer and is the foreign key of the user model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # Title is a string value that allows 100 characters is indexed and not allowed to be empty
    title = db.Column(db.String(100), index=True, nullable=False)
    # Description is a string value that allows 400 characters is indexed and is allowed to be empty
    description = db.Column(db.String(400), index=True, nullable=True)

    def json_dump(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            description=self.description
        )

    def __repr__(self):
        return '<ToDo Title %r>' % self.title
