#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = {}

    for x, val in a_dictionary.items():
        n_dict[x] = val * 2
    return n_dict
