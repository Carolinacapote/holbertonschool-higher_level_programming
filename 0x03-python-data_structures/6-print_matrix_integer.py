#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for digit in i:
            print("{:d}".format(digit), end=" ")
        print()
