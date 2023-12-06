#!/usr/bin/python3
"""Defining Write_file module"""


def write_file(filename="", text=""):
    """Writing string to UTF8 file"""

    with open(filename, "w", encoding="utf-8") as mfl:
        return mfl.write(text)
