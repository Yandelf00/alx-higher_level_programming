#!usr/bin/python3
"""square"""

Rectangle = __import__('9-rectangle.py').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
	"""square"""
	def __init__(self, size):
		def __init__(self, size):
        """ initialize """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
