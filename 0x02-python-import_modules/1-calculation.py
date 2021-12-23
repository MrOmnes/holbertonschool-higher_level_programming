#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    print("{}".format(str(a)), "+", "{}".format(str(b)), "=", add(a, b))
    print("{}".format(str(a)), "-", "{}".format(str(b)), "=", sub(a, b))
    print("{}".format(str(a)), "*", "{}".format(str(b)), "=", mul(a, b))
    print("{}".format(str(a)), "/", "{}".format(str(b)), "=", div(a, b))
