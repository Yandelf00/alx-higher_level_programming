#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests as reqs
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    json_data = {"q": letter}
    try:
        resp = reqs.post(url, data=json_data)
        resp.raise_for_status()
        js_data = resp.json()
        if js_data == {}:
            print("No result")
        else:
            print(f"[{js_data.get('id')}] {js_data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
