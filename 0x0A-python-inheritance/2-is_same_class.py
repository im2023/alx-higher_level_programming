#!/usr/bin/python3
"""Returning specific class instance"""


def is_same_class(obj, a_class):
    """Checking object instance of a given class.
    Arguments:
        obj (any): object to check.
        a_class (type): Comparing class to the type of obj to.
    Returning:
        the Boolean instance of a_class
    """
    if type(obj) is a_class:
        return True
    return False
