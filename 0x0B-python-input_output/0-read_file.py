#!/usr/bin/python3
"""readfile function"""


def read_file(filename=""):
    """readfile"""
    if filename == "":
        return
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
