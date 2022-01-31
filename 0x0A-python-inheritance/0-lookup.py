#!/usr/bin/python3
"""0-lookup.py:
    Print all attributes of an objects
"""


def lookup(obj):
    """
    Return Attribute
    """
    attributes = dir(obj)
    return(attributes)
