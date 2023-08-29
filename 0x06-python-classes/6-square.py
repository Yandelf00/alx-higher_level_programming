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

    @property
    def position(self):
        """Sets value of position.

        Args:
            value (int): square position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets value into position.

        Args:
            value (int): square position.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print()
            sqr_pattern = " " * self.__position[0] + "#" * self.__size + "\n"
            print(sqr_pattern * self.__size, end="")
