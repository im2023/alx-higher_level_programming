#!/usr/bin/python3
class Square:
    """
    class representing a square and provides methods to work.
    """

    def __init__(self, size=0):
        """
        Creating new square.

        Args:
            size (int):length of side of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size (length of a side) of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set.
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
