#!/usr/bin/python3
"""
    Module that creates a function: write_file
"""


def write_file(filename="", text=""):
    """
        function that writes a string to a text file
        (UTF8) and returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
    