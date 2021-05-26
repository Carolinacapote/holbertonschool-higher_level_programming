#!/usr/bin/python3
"""This module contains a function called text_indentation(), that prints a
text with 2 lines after each of these characters: '.', '?' and ':'
The function returns nothing.
"""


def text_indentation(text):
    """
    Args:
        text (str): Text to be printed.

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    indented_line = ''
    for character in text:

        if character in ['.', '?', ':']:
            indented_line += character
            print(indented_line.strip(' '))
            print()
            indented_line = ''

        else:
            indented_line += character

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
