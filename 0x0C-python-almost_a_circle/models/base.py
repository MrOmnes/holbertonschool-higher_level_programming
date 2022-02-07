#!/usr/bin/python3
"""Base class"""


class Base:
    """nb object to set an id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init of the Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
