#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    newstr = ""
    for c in str:
        if x != n:
            newstr += c

        x += 1

    return
