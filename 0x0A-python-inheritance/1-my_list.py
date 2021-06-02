#!/usr/bin/python3
"""TThis module contains a class *MyList* that inherits from list"""


class MyList(list):
    """ Class that inherits from list"""

    # Public instance method.
    def print_sorted(self):
        """It prints the list, but sorted"""
        print(sorted(self))
