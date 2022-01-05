#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = len(my_list)
    c = 0
    d = 0
    checker = []
    while i != 0:
        if my_list[c] not in checker:
            checker.append(my_list[c])
            d += my_list[c]
        i -= 1
        c += 1
    return d
