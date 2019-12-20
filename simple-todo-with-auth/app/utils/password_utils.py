#!/usr/bin/python3
# Some password utilities
"""
 Author: Daniel Córdova A.
"""
import hashlib


# Function that return the password after making a sha512
def get_hashed_password_with_sha512(string_password):
    hash_object = hashlib.sha512(string_password.encode('utf-8'))
    return hash_object.hexdigest()
