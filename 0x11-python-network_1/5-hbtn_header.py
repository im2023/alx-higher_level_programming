#!/usr/bin/python3
"""
taking in URL, sending request to URL and displays value
of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    re = requests.get(argv[1])
    print(re.headers.get('X-Request-Id'))
