#!/usr/bin/python3
"""
    This module contain an empty Rectangle class with
    width and height attributes and also a proprety and
    proprety setter.
    Also has two public instance methods to get the area
    and perimeter of the rectangle that can be printed
    with print
"""


class Rectangle:
    """
        An rectangle class with width and height properties
        and a area and perimeter methods
    """

    def __init__(self, width=0, height=0):
        """ Initialize a new instance """

        self.width = width
        self.height = height

    def __str__(self):
        """ Returns the string representation """

        string = ""
        if self.__height == 0 or self.__width == 0:
            return string

        for x in range(self.__height):
            for y in range(self.width):
                string += '#'
            string += '\n'

        return string[:-1]

    @property
    def width(self):
        """ get the width proprety """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width proprety """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ get the height proprety """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height proprety """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns area of the rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns perimeter of the rectangle """

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)