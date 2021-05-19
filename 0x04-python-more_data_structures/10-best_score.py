#!/usr/bin/python3
"""This module returns the key with the highest score."""


def best_score(a_dictionary):
    """The function gets the highest value of the keys in a dictionary.

args:
    a_dictionary. Dictionary to be used
"""
    if a_dictionary is not None:
        try:
            return(max(a_dictionary, key=a_dictionary.get))
        except ValueError:
            return None
            pass

    else:
        return None
