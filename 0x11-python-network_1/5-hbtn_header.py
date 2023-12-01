#!/usr/bin/python3
""" Use requests to get response and search key using get """
import requests as reqs
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    resp = reqs.get(url)
    print(resp.headers.get('X-Request-Id'))
