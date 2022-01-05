#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    i = len(matrix)
    c = 0
    while i != 0:
        new_matrix[c] = pow(new_matrix[c], 2)
        i -= 0
        c += 1
    return