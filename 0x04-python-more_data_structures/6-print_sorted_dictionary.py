#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())

    for allias in sort:
        val = a_dictionary[allias]
        print("{}: {}".format(allias, val))
