#!/usr/bin/python3
"""the append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """the class body."""
    txt = ""
    with open(filename) as x:
        for l in x:
            txt += l
            if search_string in l:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
