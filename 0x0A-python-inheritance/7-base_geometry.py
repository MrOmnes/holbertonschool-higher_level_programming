#!/usr/bin/python3
"""7-base_geometry.py:
    Empty Class that raise an exception and verify and integer
"""


class BaseGeometry:
    """Empty Class that raise an exception and verify and integer"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verify an integer"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        return value
