#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    c = i
    i = 0
    while c != 0:
        if ord(str[i]) in range(97, 123):
            stro = ord(str[i]) - 32
            print(chr(stro), end="")
        else:
            print((str[i]), end="")
        i += 1
        c -= 1
    print("")
