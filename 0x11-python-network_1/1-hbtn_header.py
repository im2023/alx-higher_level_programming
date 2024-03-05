#!/usr/bin/python3
"""
taking in a URL, sends a request to the URL and
displays the value of the X-Request-Id.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    r = urllib.request.Request(argv[1])
    with urllib.request.urlopen(r) as resp:
        print(resp.getheader('X-Request-Id'))
