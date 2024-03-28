#!/usr/bin/python3

"""
Script takes user's GitHub credentials and uses the GitHub API
to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    verify = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=verify)
    print(response.json().get("id"))
