#!/usr/bin/python3
"""
This module contains a function 'matrix_divided()'.

matrix_divided() - Function that divides all elements of a matrix
by a specific number.
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list): It is an array of lists of integers/floats.
        div (int): the arguments are divided by this number.
    Returns:
        A new matrix with the results of the divisions.
    """
    error_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(error_msg)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_mtx = matrix.copy()

    if len(new_mtx) == 1:
        raise TypeError(error_msg)

    for i in new_mtx:

        count = 0
        if type(i) is not list:
            raise TypeError(error_msg)

        if len(i) != len(new_mtx[count + 1]):
            raise TypeError('Each row of the matrix must have the same size')

        for num in i:
            if type(num) not in [int, float]:
                raise TypeError(error_msg)

    return list([(round((num / div), 2)) for num in i] for i in new_mtx)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
