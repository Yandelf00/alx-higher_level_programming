#!/usr/bin/python3
""" Use requests to get response"""
import requests as req


if __name__ == "__main__":
    res = req.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
