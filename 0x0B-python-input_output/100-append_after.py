#!/usr/bin/python3
"""This module contains a function called append_after that inserts
a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename (str): file to be opened and used.
        search_string (str): String to be found into the document.
        new_string (str): String to be append after the search_string.
    """
    file_copy = ""
    with open(filename) as my_file:
        for string in my_file:
            file_copy += string

            if search_string in string:
                file_copy += new_string

    with open(filename, mode='w') as my_file:
        my_file.write(file_copy)
