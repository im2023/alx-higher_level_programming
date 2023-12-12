#!/usr/bin/python3
"""Defining the Base class"""
import csv
import turtle
from json import dumps, loads


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
        """convert the result to Json."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list object to json."""
        flnm = cls.__name__ + ".json"
        with open(flnm, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                dict_list = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(dict_list))
