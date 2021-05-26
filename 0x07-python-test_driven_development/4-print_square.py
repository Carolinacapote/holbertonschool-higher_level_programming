#!/usr/bin/python3
"""This module contains a function called print_square(),
that prints a square with the character #
"""


def print_square(size):
    """
    Args:
        size (int): is the size length of the square.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')

    elif size < 0:
        raise TypeError('size must be >= 0')

    elif size == 0:
        pass

    else:
        for i in range(size):
            print('#' * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
