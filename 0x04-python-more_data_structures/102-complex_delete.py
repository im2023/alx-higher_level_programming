#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = [kadnas for kadnas, vall in a_dictionary.items() if vall == value]

    for key in del_keys:
        del a_dictionary[key]

    return a_dictionary
