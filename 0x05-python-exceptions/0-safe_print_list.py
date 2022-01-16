#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = x
    c = 0
    while count != 0:
        try:
            print("{}".format(int(my_list[c])), end="")
            c += 1
            count -= 1
        except:
            print("")
            return c
    print("")
    return c