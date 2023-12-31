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
        self.setter_valid("width", value)
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
        self.setter_valid("height", value)
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
        self.setter_valid("x", value)
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
        self.setter_valid("y", value)
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle (height * width)
        """
        return self.height * self.width

    def display(self):
        """
        Printing stdout representation of rectangle.
        """
        r = ""
        print("\n" * self.y, end="")
        for t in range(self.height):
            r += (" " * self.x) + ("#" * self.width) + "\n"
        print(r, end="")

    def update(self, *args, **kwargs):
        """
        Updating arguments props in the class.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Returning dictionary representation.
        """
        return {
            "x": getattr(self, "x"),
            "y": getattr(self, "y"),
            "id": getattr(self, "id"),
            "height": getattr(self, "height"),
            "width": getattr(self, "width"),
        }

    @staticmethod
    def setter_valid(atrb, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(atrb))
        if atrb == "x" or atrb == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(atrb))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(atrb))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
