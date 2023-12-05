#!/usr/bin/python3
"""class MyInt inherits from int"""


class MyInt(int):
    """the class body of MyInt"""

    def __eq__(self, value):
        """the override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """the override != operator with =="""
        return self.real == value
