#!/usr/bin/python3
"""Defining Rectangle class"""


class Rectangle:
    """Rectangle class defined"""

    def __init__(self, width=0, height=0):
        """Initialization of Rectangle instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Seting the width of a Rectangle
        Arguments:
            value: value of the width
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Retrieving height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Seting height of the Rectangle instance.
        Arguments:
            value: height value.
        """
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
