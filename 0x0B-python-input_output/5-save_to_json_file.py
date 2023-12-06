#!/usr/bin/python3

"""Defining save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """Writing an Object to text file"""

    with open(filename, mode="w", encoding="utf-8") as flnm:
        json.dump(my_obj, flnm, ensure_ascii=False)
