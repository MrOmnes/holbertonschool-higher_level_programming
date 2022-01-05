#!/usr/bin/python3
def best_score(a_dictionary):
    i = len(a_dictionary)
    c = 0
    score = 0
    while i != 0:
        if a_dictionary.get[c] > score:
            score = a_dictionary.get[c]
        i -= 1
        c += 1
    return score