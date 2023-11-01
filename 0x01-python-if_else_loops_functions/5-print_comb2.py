#!/usr/bin/python3
for X in range(100):
    print("{:02d}".format(X), end="\n" if X == 99 else ", ")
