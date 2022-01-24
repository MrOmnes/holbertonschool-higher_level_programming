#!/usr/bin/python3
"""1-rectangle.py:
    This is just a Rectangle
"""


class Rectangle:
    """Class that print a Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        """
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is int and height >= 0:
            self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        elif type(width) is int and width >= 0:
            self.__width = width

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
