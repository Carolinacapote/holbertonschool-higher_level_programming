#!/usr/bin/python3
""" Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Module of the function write_file.

    Args:
        filename (str): file to be used.
        text (str): text to be written into the file.

    Returns: Number of characters written.
    """
    with open(filename, mode="w") as the_file:
        number_chars_written = the_file.write(text)
        return(number_chars_written)
