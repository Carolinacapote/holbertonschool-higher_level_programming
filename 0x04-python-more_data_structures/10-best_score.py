#!/usr/bin/python3
"""This module returns the key with the highest score."""


def best_score(a_dictionary):
    """The function gets the highest value of the keys in a dictionary.

args:
    a_dictionary. Dictionary to be used
"""
    if a_dictionary is not None:
        return(max(a_dictionary))

    else:
        return None
