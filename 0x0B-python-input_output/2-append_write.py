#!/usr/bin/python3
"""Append on a file"""


def append_write(filename="", text=""):
    """Append on a file"""
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
