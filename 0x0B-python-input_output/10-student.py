#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """
    Public instance attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation of a
        Student instance.
        """
        result = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str):
                    try:
                        result[attr] = getattr(self, attr)
                    except:
                        pass
        else:
            result = self.__dict__

        return result
