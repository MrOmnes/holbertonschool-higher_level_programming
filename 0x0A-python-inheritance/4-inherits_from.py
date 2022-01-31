#!/usr/bin/python3
"""Check if is inherits from"""


def inherits_from(obj, a_class):
    """Check if is inherits from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
