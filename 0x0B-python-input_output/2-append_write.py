#!/usr/bin/python3
"""Defining module appends string"""


def append_write(filename="", text=""):
    """Appending string to end of UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as mfl:
        return mfl.write(text)
