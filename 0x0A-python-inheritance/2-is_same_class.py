#!/usr/bin/python3
"""This module contains a function called *is_same_class* that proves
if an object is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: Any type of object.
        a_class: Some type of class.

    Returns:
        True: if the obj is an instance of a_class.
        False: otherwise.
    """
    if type(obj) is a_class:
        return True

    else:
        return False
