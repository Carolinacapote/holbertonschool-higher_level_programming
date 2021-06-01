#!/usr/bin/python3
"""This module contains a function that returns a list of lists
of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """
    Args:
        n (int): Integer to be used.
    Returns:
        - An empty list if n <= 0
        - A list of lists of integers if its worked.
    """
    my_list = []

    if n <= 0:
        return my_list

    else:
        x = [1]
        y = [0]

        for row_triangle in range(n):
            my_list += [x]

            x = [left+right for left, right in zip(x + y, y + x)]

        return my_list
