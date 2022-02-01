#!/usr/bin/python3
"""Write in a file"""


def write_file(filename="", text=""):
    """Write in a file"""
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
