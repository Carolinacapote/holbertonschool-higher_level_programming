#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename (str): File to be used.
    """
    with open(filename, mode="r") as the_file:
        return(json.load(the_file))
