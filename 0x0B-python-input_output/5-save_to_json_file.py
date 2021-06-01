#!/usr/bin/python3
""" Function that writes an Object to a text file, using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: object to be used.
        filename (str): file to be used
    """
    with open(filename, mode="w") as the_file:
        json.dump(my_obj, the_file)
