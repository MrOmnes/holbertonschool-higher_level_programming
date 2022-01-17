#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    value = 0
    i = x
    count = 0
    c = 0
    for size in my_list:
        c += 1
    while i != 0:
        try:
            print("{:d}".format(my_list[value]), end="")
            i -= 1
            value += 1
            count += 1
        except TypeError:
            i -= 1
            value += 1
        except ValueError:
            i -= 1
            value += 1
    print()
    return count
