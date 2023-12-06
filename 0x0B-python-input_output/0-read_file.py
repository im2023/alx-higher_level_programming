#!/usr/bin/python3
"""Defining read_file module"""


def read_file(filename=""):
    """
    read_file reading text file UTF8
    and printing result.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
