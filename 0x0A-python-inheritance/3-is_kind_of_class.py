#!/usr/bin/python3
"""class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checking instance or inherited instance of class.
    Args:
        obj (any): object checked.
        a_class (type): class compared .
    Returns:
        Boolean of an instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
