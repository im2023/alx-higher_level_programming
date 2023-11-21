#!/usr/bin/python3

"""The definition of square class"""


class Square:
    """the class body"""

    def __init__(self, size=0):
        """the Squar class contructor
        Arguments:
            size (int):size of new square.
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
