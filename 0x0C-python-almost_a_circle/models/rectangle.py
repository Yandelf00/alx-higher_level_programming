#!usr/bin/python3
"""class rectangle"""


from base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets x value """
        return self.__x

    @x.setter
    def x(self, value):
        """sets x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area"""
        return self.width * self.__height

    def display(self):
        """display func"""
        for v_shift in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ __str__ method """
        string = "[{:s}] ({:d})".format(type(self).__name__, self.id)
        string += " {:d}/{:d} ".format(self.__x, self.__y)
        string += "- {:d}/{:d}".format(self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """ update class """
        argCount = len(args)
        if argCount == 0:
            if "id" in kwargs.keys():
                super().__init__(kwargs["id"])
            if "width" in kwargs.keys():
                self.width = kwargs["width"]
            if "height" in kwargs.keys():
                self.height = kwargs["height"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
        if argCount > 0:
            super().__init__(args[0])
        if argCount > 1:
            self.width = args[1]
        if argCount > 2:
            self.height = args[2]
        if argCount > 3:
            self.x = args[3]
        if argCount > 4:
            self.y = args[4]

    def to_dictionary(self):
        """ to dictionary """
        dict_rec = {"x": self.__x, "y": self.__y, "id": self.id}
        dict_rec["width"] = self.__width
        dict_rec["height"] = self.__height
        return dict_rec
