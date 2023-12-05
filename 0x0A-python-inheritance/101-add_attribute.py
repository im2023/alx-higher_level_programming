#!/usr/bin/python3
"""Defining the function attributes"""


def add_attribute(obj, att, value):
    """Adding new attribute to object if possible
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
