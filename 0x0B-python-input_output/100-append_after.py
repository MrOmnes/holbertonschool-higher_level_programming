#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    i = 0
    with open(filename, "r+") as f:
        for line in f:
            i += 1
            if search_string in f.read():
                f.close
                with open(filename, "a") as f:
                    f.writelines(new_string)