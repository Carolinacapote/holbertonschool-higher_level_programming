#!/usr/bin/python3
"""This module contains a function called add_integer().

The function adds 2 integers.
Return the result of the addition.
"""


def add_integer(a, b=98):
    """
    Args:
        a (int or float): First number to be added.
        b (int or float): Second number to be added.
    Returns:
        int: The result of the a + b.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    else:
        if type(a) is float:
            a = int(a)

        if type(b) is float:
            b = int(b)

        return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
