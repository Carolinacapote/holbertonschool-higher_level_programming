#!/usr/bin/python3
"""This module contains a function that prints:

My name is <first name> <last name>
The functions also works without last name parameter.
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): Name to be printed
        last_name (str): Last name to be printed
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')

    else:
        print('My name is {} {}'.format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
