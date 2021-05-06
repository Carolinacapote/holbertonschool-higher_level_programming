#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    return list([(num ** 2) for num in i] for i in new_matrix)
