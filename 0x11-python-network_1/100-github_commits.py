#!/usr/bin/python3

"""
Script takes 2 arguments repository name and owner name
then displays the commits of the repository
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo_owner, repo_name)
    req = requests.get(url)
    commits = req.json()
    try:
        for _ in range(10):
            print("{}: {}".format(
                commits[_].get("sha"),
                commits[_].get("commit").get("author").get("name")))
    except IndexError:
        pass
