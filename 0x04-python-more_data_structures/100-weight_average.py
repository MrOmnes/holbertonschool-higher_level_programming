#!/usr/bin/python3
def weight_average(my_list=[]):
    c = 0
    result = 0
    i = len(my_list)
    if len(my_list) == 0:
        return 0
    while i != 0:
        result += my_list[c]
        i -= 1
        c += 1
    result = result / c
    return result