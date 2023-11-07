#!/usr/bin/python3


def no_c(my_string):
    x = ""
    for c in my_string:
        if c != "c" and c != "C":
            x += c

    return x
