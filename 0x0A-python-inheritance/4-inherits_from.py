#!/usr/bin/python3
"""Defining inherited class-checking method"""


def inherits_from(obj, a_class):
    """Checks if object is the inherited instance of class.
    Arguments:
        obj (any): object to check
        a_class (type): Compared class
    Returns:
        boolean of inheritance(true/false)
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
