#!/usr/bin/python3

"""
Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        print("No result")
    else:
        req = requests.post(url, data={'q': argv[1]})
        try:
            result = req.json()
            if result:
                print("[{}] {}".format(result.get('id'), result.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
