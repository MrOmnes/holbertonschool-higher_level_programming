#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    c = len(my_list)
    new_list = []
    while c > 0:
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
        c -= 1
    return new_list
