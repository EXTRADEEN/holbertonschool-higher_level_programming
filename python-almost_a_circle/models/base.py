#!/usr/bin/python3
"""
    Module that creates a new class: Base
"""


class Base:
    """ private class attribute __nb_objects that is set to 0 """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
