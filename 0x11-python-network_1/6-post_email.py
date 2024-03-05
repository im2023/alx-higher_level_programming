#!/usr/bin/python3
"""
giving URL & email, sending POST req to URL.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    l = {'email': argv[2]}
    req = requests.post(url, data=l)
    print(req.text)
