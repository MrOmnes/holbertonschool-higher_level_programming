#!/usr/bin/python3
"""3-is_kind_of_class.py:
    Check if obj is kind of a_class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is kind of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
