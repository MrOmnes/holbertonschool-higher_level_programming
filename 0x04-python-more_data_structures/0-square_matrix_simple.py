#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    i = len(matrix)
    c = 0
    while i != 0:
        new_matrix[c] = new_matrix[c] * new_matrix[c]
        i -= 0
        c += 1
    return