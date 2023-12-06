#!/usr/bin/python3
"""the append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """the class body."""
    text = ""
    with open(filename) as x:
        for l in x:
            text += l
            if search_string in l:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
