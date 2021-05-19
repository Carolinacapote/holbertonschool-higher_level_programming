#!/usr/bin/python3
"""This module returns the key with the highest score."""


def best_score(a_dictionary):
    """The function gets the highest value of the keys in a dictionary.

args:
    a_dictionary. Dictionary to be used
"""
    max_score = {}
    if a_dictionary is None:
        return None
    for key in sorted(a_dictionary):
        max_score[key] = a_dictionary[key]
    return(key)
