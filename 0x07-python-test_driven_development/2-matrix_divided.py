#!/usr/bin/python3
def matrix_divided(matrix, div):
    i = 0
    c = len(matrix)
    resultmatrix = ()
    while c != 0:
        resultmatrix += (int(matrix[i]) / div)
        c -= 1
        i += 1
    return resultmatrix