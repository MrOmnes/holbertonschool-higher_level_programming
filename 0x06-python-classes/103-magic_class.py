#!/usr/bin/python3
"""3-square.py:
    This is just a Square
"""


import math


class MagicClass:
    """
    Definie the size of the square

    Attributes
    ----------
    size : int
        The size of the square.
    """
    def __init__(self, radius=0):
        """
        Parameters
        ----------
        radius : int
            The size of the square.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (self.__radius * 2 * math.pi)
