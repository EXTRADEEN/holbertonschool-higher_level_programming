#!/usr/bin/bash
"""
    Module that checks instance of a specified class
"""


def is_same_class(obj, a_class):
    """ Checks if the object is exactly an instance of the specified class """

    return type(obj) is a_class
