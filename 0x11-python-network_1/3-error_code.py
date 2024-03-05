#!/usr/bin/python3
"""
given URL, sends a request, displays response (utf-8).
usage: ./3-error_code.py http://0.0.0.0:5000/status_401
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            print(resp.read().decode())
    except urllib.error.URLError as ex:
        print("Error code: {}".format(ex.code))
