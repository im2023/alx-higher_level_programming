#!/usr/bin/python3
"""load_from_json module"""
import json


def load_from_json_file(filename):
    """loading from json to the file"""
    with open(filename, encoding="utf-8") as load_fl:
        return json.load(load_fl)
