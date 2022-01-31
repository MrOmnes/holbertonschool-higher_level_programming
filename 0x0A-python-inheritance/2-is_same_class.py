#!/usr/bin/python3
"""2-is_same_class.py:
    Check if obj are same class than a_class
"""


def is_same_class(obj, a_class):
    """
    Check if obj are same class than a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
