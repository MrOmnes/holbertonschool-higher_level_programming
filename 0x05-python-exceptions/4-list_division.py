#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = list_length
    i = 0
    result = []
    while c != 0:
        try:
            result += [my_list_1[i] / my_list_2[i]]
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            c -= 1
            i += 1
    return result
