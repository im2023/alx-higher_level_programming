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

    @staticmethod
    def from_json_string(json_string):
        """Returning the deserialization of a JSON"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returning the class instantiated from a dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                x = cls(1, 1)
            else:
                x = cls(1)
            x.update(**dictionary)
            return x

    @classmethod
    def load_from_file(cls):
        """Returning list of classes instantiated from file of JSON"""
        fil = str(cls.__name__) + ".json"
        try:
            with open(fil, "r") as json_fl:
                list_dicts = Base.from_json_string(json_fl.read())
                return [cls.create(**n) for n in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writing CSV of list of objects to a file"""
        fil = cls.__name__ + ".csv"
        with open(fil, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    filenames = ["id", "width", "height", "x", "y"]
                else:
                    filenames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=filenames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of class instantiated from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
