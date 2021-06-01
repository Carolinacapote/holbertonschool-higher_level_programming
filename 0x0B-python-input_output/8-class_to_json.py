#!/usr/bin/python3
"""function that returns the dictionary description"""


def class_to_json(obj):
    """
    function that returns the dc
    """
    return obj.__dict__
