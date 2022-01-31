#!/usr/bin/python3
"""100-my_int.py:
    MyInt is a rebel
"""


class MyInt(int):
    """My Int is a rebel"""
    def __eq__(self, other):
        """Check equality"""
        return int.__index__ == other

    def __ne__(self, other):
        """Check inequality"""
        return int.__index__ != other
