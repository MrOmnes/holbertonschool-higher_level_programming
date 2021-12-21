#!/usr/bin/python3
i = 0
c = 122
d = 89
while i != 26:
    if i % 2 == 0:
        print("{}".format(chr(c)), end="")
        c -= 2
    else:
        print("{}".format(chr(d)), end="")
        d -= 2
    i += 1
