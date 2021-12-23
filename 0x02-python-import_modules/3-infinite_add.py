#!/usr/bin/python3
import sys
c = len(sys.argv) - 1
d = 1
total = 0
if __name__ == '__main__':
    while c != 0:
        total = total + int(sys.argv[d])
        d += 1
        c -= 1
    print(total)
