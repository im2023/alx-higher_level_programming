#!/usr/bin/python3
"""
fetching https://alx-intranet.hbtn.io/status.
"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as answer:
    body = answer.read()
print('Body response:')
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
