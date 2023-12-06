#!/usr/bin/python3
"""The class-to-JSON module"""


def class_to_json(obj):
    """Returns the dictionary rep of json"""
    return obj.__dict__
