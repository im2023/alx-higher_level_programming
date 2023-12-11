#!/usr/bin/python3
"""the module for rectangle class"""


from models.base import Base


class Rectangle(Base):
    """the rectangle class bese class implement"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns private attribute (__width).
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting attribute (__width).
        """
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Return private attribute (___height).
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting attribute (__height)
        """
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Return private attribute (__x).
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setting the attribute (__x).
        """
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Return private attribute (__y).
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setting attribute (__y).
        """
        self.setter_validation("y", value)
        self.__y = value
