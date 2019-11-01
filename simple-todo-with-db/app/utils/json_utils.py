#!/usr/bin/python3
# Some utilities
"""
 Author: Daniel Córdova A.
"""

from flask import abort


def is_not_json_request(request):
    if not request.json:
        abort(400)
