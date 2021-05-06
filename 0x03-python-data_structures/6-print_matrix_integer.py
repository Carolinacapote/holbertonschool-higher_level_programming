#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if i:
            for digit in i:
                print("{:d}".format(digit), end=" ")
        print()
