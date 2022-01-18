#!/usr/bin/python3
"""3-square.py:
    This is just a Square
"""


class Square:
    """
    Definie the size of the square

    Attributes
    ----------
    size : int
        The size of the square.
    """
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int
            The size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) == int and size >= 0:
            self.__size = size

    @property
    def size(self):
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif type(self.__size) == int:
            return self.__size

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif type(value) == int:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        c = self.__size
        i = self.__size
        while c != 0:
            print('#', end="")
            c -= 1
            if i != 1 and c == 0:
                print("")
                i -= 1
                c = self.__size
        print("")
