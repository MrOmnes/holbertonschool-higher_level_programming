#!/usr/bin/python3
"""1-my_list.py:
    Print my list in order
"""


class MyList(list):
    """Class that print a list in order"""
    def print_sorted(self):
        """
           Print a list sorted
        """
        print(sorted(self))
