#!/usr/bin/python3
def remove_char_at(str, n):
    s = 0
    new_string = ""
    for x in str:
        if s != n:
            new_string += x

        s += 1
    return
