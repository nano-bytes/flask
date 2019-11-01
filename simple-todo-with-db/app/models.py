#!/usr/bin/python3
# Models for Series MicroService
"""
 Author: Daniel Córdova A.
"""

from app import db


# This class contains the model that will create a table inside our Database
class ToDo(db.Model):
    # Id is a integer and is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Title is a string value that allows 100 characters is indexed and not allowed to be empty
    title = db.Column(db.String(100), index=True, nullable=False)
    # Description is a string value that allows 400 characters is indexed and is allowed to be empty
    description = db.Column(db.String(400), index=True, nullable=True)

    def json_dump(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description
        )

    def __repr__(self):
        return '<ToDo Title %r>' % self.title
