#!/usr/bin/python3
# Runner module
"""
 Author: Daniel Córdova A.
"""

import os
from app import app

app.debug = True
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8085))

app.run(host=host, port=port)
