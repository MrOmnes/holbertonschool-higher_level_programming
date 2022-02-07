#!/usr/bin/python3
"""Base class"""


import json


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

    def to_json_string(list_dictionaries):
        """To Json String"""
        try:
            return json.dumps(list_dictionaries)
        except Exception:
            return []
