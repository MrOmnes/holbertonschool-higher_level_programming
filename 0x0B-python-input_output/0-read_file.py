#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, "r") as f:
        print(f.read())
