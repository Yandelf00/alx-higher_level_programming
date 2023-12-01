#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests as reqs
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    resp = reqs.get(url)
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.text)
