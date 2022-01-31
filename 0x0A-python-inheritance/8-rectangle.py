#!/usr/bin/python3
"""8-base_geometry.py:
    Set size of a rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Set the size of a rectangle"""
    def __init__(self, width, height):
        """Init the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
