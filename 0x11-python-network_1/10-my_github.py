#!/usr/bin/python3
"""get id from your github"""
import requests as reqs
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = reqs.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))
