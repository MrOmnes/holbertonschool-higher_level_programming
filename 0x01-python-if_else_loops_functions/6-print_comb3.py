#!/usr/bin/python3
c = 0
d = 0

while c < 9:
    d = c + 1
    while d <= 9:
        print(str(c)+str(d), end='')
        if c != 8:
            print(', ', end='')
        d += 1
    c += 1
print('')
