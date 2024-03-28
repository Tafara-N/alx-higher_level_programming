#!/usr/bin/python3

"""
Script sends an HTTP Request to a URL and prinyt out the response
"""

import requests

response = requests.get("http://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
