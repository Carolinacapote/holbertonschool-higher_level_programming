#!/usr/bin/python3
"""This module contains a function called *is_kind_of_class* that checks
if an object is an instance of, or if the object is an instance of a class
that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: Any type of object.
        a_class: Some type of class.

    Returns:
        True: if the obj is an instance of a_class or of a class that
        inherited from.
        False: otherwise.
    """
    if isinstance(obj, a_class) is True:
        return True

    else:
        return False
