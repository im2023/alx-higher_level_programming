#!/usr/bin/python3
"""Defining to_json_string module"""

import json


def to_json_string(my_obj):
    """returning the JSON rep. object (string)"""

    return json.dumps(my_obj)
