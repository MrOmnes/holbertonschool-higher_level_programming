#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_r = set_1 - set_2
    set_r.update(set_2 - set_1)
    return set_r
