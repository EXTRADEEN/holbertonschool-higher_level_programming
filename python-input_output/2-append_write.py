#!/usr/bin/python3
"""
    Module that creates a function: append_write
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text
        file (UTF8) and returns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
