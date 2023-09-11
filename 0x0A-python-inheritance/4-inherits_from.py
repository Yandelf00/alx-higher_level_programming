#!/usr/bin/python3
"""function checks if its inheritance of a class"""


def inherits_from(obj, a_class):
    """checks if its inheritance of a class"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
