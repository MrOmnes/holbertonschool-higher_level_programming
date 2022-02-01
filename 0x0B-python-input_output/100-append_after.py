#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, "a+") as f:
        if search_string in f:
            f.write(new_string)
