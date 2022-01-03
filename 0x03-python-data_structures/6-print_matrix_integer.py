#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = -1
    while matrix[a:]:
        a += 1
        b = 0
        while matrix[a:b]:
            print(matrix[a:b])
            b += 1
