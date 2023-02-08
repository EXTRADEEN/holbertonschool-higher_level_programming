#!/usr/bin/python3
"""
    Module that checks instance of a specified class
"""


def inherits_from(obj, a_class):
    """ Checks if the object is an instance of a class
    that inherited (directly or indirectly) from
    the specified class """

    return isinstance(obj, a_class) and not type(obj) is a_class
