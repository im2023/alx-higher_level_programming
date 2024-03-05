#!/usr/bin/python3
"""
taking in a URL and an email, sends a POST request to the passed URL
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    u = argv[1]
    val = {'email': argv[2]}

    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    r = urllib.request.Request(u, data)
    with urllib.request.urlopen(r) as resp:
        print(resp.read().decode())
