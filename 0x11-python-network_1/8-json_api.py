#!/usr/bin/python3
"""
giving letter as parametr,and posting to:
 http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
