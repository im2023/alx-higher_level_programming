#!/usr/bin/python3
"""Defining the Base class"""
import json
import csv
import turtle


class Base:
    """representation of the Base class body"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converting the result to Json."""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)
