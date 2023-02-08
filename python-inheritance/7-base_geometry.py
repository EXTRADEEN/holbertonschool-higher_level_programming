#!/usr/bin/python3
"""
    Module that creates a class: BeseGeometry
"""


class BaseGeometry:
    """ Defines the class: BaseGeometry """

    def area(self):
        """ returns the area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
