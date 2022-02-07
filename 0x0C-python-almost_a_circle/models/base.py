#!/usr/bin/python3
"""Base class"""


import json
from queue import Empty


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
        if list_dictionaries is None or list_dictionaries is Empty:
            return []
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ Save to file """
        with open(cls.__name__ + ".json", "w+") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json.dumps(list_objs))

    def from_json_string(json_string):
        """ From Json to string """
        if json_string is Empty or json_string is None:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """Dictionnary to object"""
        for key in dictionary:
            setattr(cls, key, dictionary[key])

    def load_from_json_file(cls):
        """Load from a json file"""
        with open(cls+".json", "r") as f:
            try:
                return json.load(f)
            except Exception:
                return []
