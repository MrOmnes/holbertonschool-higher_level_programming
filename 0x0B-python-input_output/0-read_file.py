#!/usr/bin/python3
"""Read a file"""
def read_file(filename=""):
    """Read a file"""
    with open('my_file_0.txt') as f:
        print(f.read())
