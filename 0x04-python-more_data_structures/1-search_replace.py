#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return

    new_lst = my_list[:]
    for x, y in enumerate(new_lst):
        if y == search:
            new_lst[x] = replace

    return new_lst
