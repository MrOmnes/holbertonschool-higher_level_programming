#!/usr/bin/python3
"""Add an item to a file"""
import sys


loadfromjsonfile = __import__('6-load_from_json_file').load_from_json_file
savetojsonfile = __import__('5-save_to_json_file').save_to_json_file


def add_item(args):
    """Read a file"""
    with open("add_item.json", "a+"):
        list = loadfromjsonfile("add_item.json")
        i = len(args) - 1
        c = 1
        while(i != 0):
            list.append(args[c])
            i -= 1
            c += 1
        savetojsonfile(list, "add_item.json")


add_item(sys.argv)
