#!/usr/bin/python3
"""101-add_attribute.py:
    Add an attribute
"""


def add_attribute(obj, name, value):
    """Add an attribute if is not already in the class"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
