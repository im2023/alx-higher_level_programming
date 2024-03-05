#!/usr/bin/python3
"""
Usesing GitHub API to display GitHub ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    d = requests.get("https://api.github.com/user", auth=auth)
    print(d.json().get("id"))
