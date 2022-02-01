#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Public Init of first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict"""
        return self.__dict__
