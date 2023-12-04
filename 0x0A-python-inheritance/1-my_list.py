#!/usr/bin/python3
"""inherits from list class Mylist"""


class MyList(list):
    """The class that inherits"""

    def print_sorted(self):
        """prints the sorted list."""
        print(sorted(self))
