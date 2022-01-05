#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    c = 0
    i = len(a_dictionary)
    while i != 0:
        a_dictionary[c] = a_dictionary[c] * 2
        c += 1
        i -= 1
    return a_dictionary
