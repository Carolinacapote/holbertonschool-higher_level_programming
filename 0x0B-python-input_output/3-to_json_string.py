#!/usr/bin/python3
""" Function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: Object yo be used.
    """
    return json.dumps(my_obj)
