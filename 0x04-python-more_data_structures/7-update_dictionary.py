#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        key = value
    else:
        a_dictionary.update(key)
    return a_dictionary