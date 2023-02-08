#!/usr/bin/python3
"""
    Module that creates a class: BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Recangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ returns the area of the square """

        return pow(self.__size, 2)

    def __str__(self):
        return "[Square] " + str(self.__size) + '/' + str(self.__size)
