#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_k = [kad for kad, va in a_dictionary.items() if va == value]

    for key in del_k:
        del a_dictionary[key]

    return a_dictionary
