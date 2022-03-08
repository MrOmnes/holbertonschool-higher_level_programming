#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    try:
        print("My name is" , first_name , last_name)
    except:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")

        if type(last_name) is not str:
            raise TypeError("last_name must be a string")