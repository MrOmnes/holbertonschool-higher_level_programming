#!/usr/bin/python3
import sys
c = len(sys.argv) - 1
d = 1
if len(sys.argv) == 0:
    print(len(sys.argv) - 1, "arguments.")
else:
    print(len(sys.argv) - 1, "arguments:")
    while(c != 0):
        print(d, ":", sys.argv[d])
        d += 1
        c -= 1
