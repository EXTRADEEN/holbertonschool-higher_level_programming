#!/usr/bin/python3
"""
    This module contain a function text_identation(text)
    that prints a text with 2 new line after each of these characters:
    '.', '?', ':'. If text is not a string a TypeError is raised.
"""


def text_indentation(text):
    """ function that prints the text """
    c = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if c == 0:
            if i == " ":
                continue
            else:
                c = 1
        if c == 1:
            if i == '.' or i == '?' or i == ':':
                print(i + '\n')
                c = 0
            else:
                print(i, end='')
