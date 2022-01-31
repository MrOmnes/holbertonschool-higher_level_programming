#!/usr/bin/python3
"""10-square.py:
    Set size and area of a rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that create a square"""
    def __init__(self, size):
        """Init the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of the square"""
        return self.__size * self.__size
