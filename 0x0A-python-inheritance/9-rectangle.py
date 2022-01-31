#!/usr/bin/python3
"""9-rectangle.py:
    Set size and area of a rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Create size and area of a rectangle"""
    def __init__(self, width, height):
        """Set width and height"""
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """Set area"""
        return self.__width * self.__height

    def __str__(self):
        """Return"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
