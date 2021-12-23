#!/usr/bin/python3
import sys
c = len(sys.argv) - 1
d = 1
if __name__ == '__main__':
    if len(sys.argv) - 1 == 0:
        print(len(sys.argv) - 1, "arguments.")
    else:
        if len(sys.argv) - 1 == 1:
            print(len(sys.argv) - 1, "argument:")
        else:
            print(len(sys.argv) - 1, "arguments:")
        while(c != 0):
            print("{}".format(str(d)) + ":", sys.argv[d])
            d += 1
            c -= 1
