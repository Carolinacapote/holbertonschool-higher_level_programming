#!/usr/bin/python3
"""This module contains a function called *lookup* that returns a list"""


def lookup(obj):
    """
    Returns:
        The list of available attributes and methods of an object.
    """
    return dir(obj)
