#!/usr/bin/python3
""" Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): file to be used.
        text (str): text to be written at the end of the file.
    """
    with open(filename, mode="a") as the_file:
        number_chars_written = the_file.write(text)
        return(number_chars_written)
