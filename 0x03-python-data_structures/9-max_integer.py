#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a = len(my_list)
    b = 0
    c = my_list[b]
    while a > 0:
        if my_list[b] > c:
            c = my_list[b]
        b += 1
        a -= 1
    return c
