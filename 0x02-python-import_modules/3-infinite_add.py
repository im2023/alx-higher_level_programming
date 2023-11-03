#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = 0
    for x in sys.argv:
        if x != sys.argv[0]:
            i += int(x)
    print(i)
