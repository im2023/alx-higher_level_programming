#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = [kadnas for kadnas, vall in a_dictionary.items() if vall == value]

    for kadnas in del_keys:
        del a_dictionary[kadnas]

    return a_dictionary
