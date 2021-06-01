#!/usr/bin/python3
""" This module contains a function that reads a text file
(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ Module of the function read_file.

    Args:
        filename (str): file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as to_print:
        file_content = to_print.read()
        print(file_content, end='')
