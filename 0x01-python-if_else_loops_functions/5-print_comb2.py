#!/usr/bin/python3
for c in range(00, 100):
    if c == 99:
        print("{}".format(int(c)), end="\n")
    else:
        print("{:02d}".format(int(c)) + ", ", end="")
