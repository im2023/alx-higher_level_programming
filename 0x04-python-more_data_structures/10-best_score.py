#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    maxy1 = None
    maxy2 = None

    for x, y in a_dictionary.items():
        if isinstance(y, int):
            if maxy2 is None or y > maxy2:
                maxy1 = x
                maxy2 = y

    return maxy1
