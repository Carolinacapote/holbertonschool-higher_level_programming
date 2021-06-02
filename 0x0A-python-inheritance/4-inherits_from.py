#!/usr/bin/python3
"""This module contains a function called *inherits_from* that checks
if the object is an instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: Any type of object.
        a_class: Some type of class.

    Returns:
        True: if the obj is an instance of a class that inherited from a_class.
        False: otherwise.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class) is True:
        return True

    else:
        return False
