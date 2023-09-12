#!/usr/bin/python3
"""appendwrite function"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
