#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests as reqs
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    resp = reqs.post(url, data={'email': email})
    print(resp.text)
