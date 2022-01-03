#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = len(my_list)
    b = 0
    while a != 0:
        print("{:d}".format(int(my_list[b])))
        a -= 1
        b += 1
