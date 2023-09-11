#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """function that raises error cuz !area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates idk"""
        if type(value) is not int:
            raise Exception(f"{name} must be an integer")
        elif value <= 0:
            raise Exception(f"{name} must be greater than 0")
