#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Public Init of first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict"""
        if type(attrs) is list:
            return (self for x in attrs if attrs)
        else:
            return self.__dict__
