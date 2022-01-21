#!/usr/bin/python3
"""0-add_integer.py:
    Function that add two integer and return an integer
	a and b
	return a + b
"""


def add_integer(a, b=98):
    """
        Function that add two integer and return an integer
        Parameters
        ----------
        a : int
            One of the int
        b : int
            The other int
        Raise
    """
    try:
        return int(a + b)
    except:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer")