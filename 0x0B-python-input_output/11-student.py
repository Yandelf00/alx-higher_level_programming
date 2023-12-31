#!/usr/bin/python3
"""student classu"""


class Student:
    """Student."""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json."""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """reload_from_json"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
