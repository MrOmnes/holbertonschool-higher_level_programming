#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) == int and size >=0:
            self.__size = size
    def area(self):
        self.area = Square.__size * Square.__size