#!/usr/bin/python3
"""6-rectangle.py:
    This is just a Rectangle
"""


class Rectangle:
    """Class that print a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ""
        return ("#" * self.__width + "\n") * \
            (self.__height - 1) + "#" * self.__width

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) is int and value >= 0:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        elif type(value) is int and value >= 0:
            self.__height = value
