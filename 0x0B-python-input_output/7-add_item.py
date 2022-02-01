#!/usr/bin/python3

loadfromjsonfile = __import__('6-load_from_json_file').load_from_json_file
savetojsonfile = __import__('5-save_to_json_file').save_to_json_file

def add_item(args):
    """Read a file"""
    with open("add_item.json", "w") as f:
        list = loadfromjsonfile(f)
        list.append(args)
        savetojsonfile(list, "add_item.json")
