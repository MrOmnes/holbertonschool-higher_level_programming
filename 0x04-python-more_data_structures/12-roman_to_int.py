#!/usr/bin/python3
def roman_to_int(roman_string):
    checker = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = len(roman_string)
    c = 0
    result = 0
    while i != 0:
        if roman_string[c] in checker:
            result += checker.get(roman_string[c])
        if result == 11:
            result = 9
        i -= 1
        c += 1
    return result
