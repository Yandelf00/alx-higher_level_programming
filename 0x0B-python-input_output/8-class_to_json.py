#!/usr/bin/python3
"""classtojson file"""


def class_to_json(obj):
    """class_to_json"""
    objct = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            objct[key] = value

    return objct
