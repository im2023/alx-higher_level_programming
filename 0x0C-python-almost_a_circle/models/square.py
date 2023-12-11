#!/usr/bin/python3
"""Defining the square class Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """the class body"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returning width size"""
        return self.width

    @size.setter
    def size(self, value):
        """Square height and width."""
        self.width = value
        self.height = value

    def __str__(self):
        """the square class string."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """updating square."""
        if len(args):
            for c, arg in enumerate(args):
                if c == 0:
                    self.id = arg
                elif c == 1:
                    self.size = arg
                elif c == 2:
                    self.x = arg
                elif c == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary of the class."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
