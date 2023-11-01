#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    new_strg = ""
    for c in str:
        if x != n:
            new_strg += c
        x += 1
    return
