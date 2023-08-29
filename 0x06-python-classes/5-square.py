#!/usr/bin/python3
"""square class"""


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
        self.__size = size

    def area(self):
        """calc area
        returns:
            return area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """get value attribute.

        Returns:
            int: the attribute value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): square size.

        Raises:
            TypeError: if not int.
            ValueError: if not positive.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with #"""
        printSize = self.__size
        if printSize == 0:
            print()
        for i in range(printSize):
            for j in range(printSize):
                print("#", end="")
            print()
