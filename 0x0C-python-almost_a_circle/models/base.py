#!/usr/bin/python3
"""This module contains a superclass called *Base*"""


class Base:
    """This class will be the "base" of the other classes (Rectangle, Square)
    """
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """
        Conditionals:
            if "id" is not None, assign the "id" with this argument value.
            Otherwise id equals to __nb_objects
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
