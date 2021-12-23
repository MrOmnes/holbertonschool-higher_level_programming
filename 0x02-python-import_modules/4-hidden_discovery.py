#!/usr/bin/python3
import hidden_4
a = dir(hidden_4)
i = 1
if __name__ == '__main__':
    while i != 12:
        if a[i][1] != '_':
            print("{}".format(str(a[i])))
            i += 1
        else:
            i += 1
