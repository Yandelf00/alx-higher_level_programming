#!/usr/bin/python3
"""our square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init square
        Args:
            size (int): square size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calc area
        returns:
            area.
        """
        return self.__size ** 2
