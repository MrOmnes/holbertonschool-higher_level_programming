#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for c in new_dictionary:
        new_dictionary[c] *= 2
    return new_dictionary
