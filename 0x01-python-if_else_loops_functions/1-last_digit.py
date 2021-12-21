#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    nm = (number * -1) % 10
else:
    nm = number % 10
ls = "Last digit of"
if nm > 5:
    print(ls, number, "is", nm, "and is greater than 5")
if nm != 0 and nm < 6:
    print(ls, number, "is", nm, "and is less than 6 and not 0")
if nm == 0:
    print(ls, number, "is", nm, "and is 0")
