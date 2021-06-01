#!/usr/bin/python3
""" Function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str (str): JSON string to be used.
    """
    return json.loads(my_str)
