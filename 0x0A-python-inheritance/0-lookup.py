#!/usr/bin/python3
"""0-lookup.py:
    Print all attributes of an objects
"""


def lookup(obj):
    attributes = dir(obj)
    return(attributes)
