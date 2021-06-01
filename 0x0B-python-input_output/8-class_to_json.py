#!usr/bin/python3
"""function that returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Args:
        obj: is an instance of a Class
    """
    return(obj.__dict__)
