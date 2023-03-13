#!/usr/bin/python3
"""
    Module that creates a function: class_to_json
"""


def class_to_json(obj):
    """ Rerturn the dictionary description with simple data structure
        (list, dictionary, string, integer an boolean) for JSON
        serialization of an object
    """

    return obj.__dict__
