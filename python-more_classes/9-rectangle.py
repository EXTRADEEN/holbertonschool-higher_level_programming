#!/usr/bin/python3
"""
    This module contain an empty Rectangle class with
    width and height attributes and also a proprety and
    proprety setter.
    The rectangle class has a public class method
    num_of_instances that increases when an new instance is
    created and reduces when an instance isdeleted.
    Also has two public instance methods to get the area
    and perimeter of the rectangle that can be printed
    with print.
"""


class Rectangle:
    """
        An rectangle class with width and height properties
        and a area and perimeter methods
    """

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare two rectangles """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ New Rectangle instance with = heght = size """

        return Rectangle (size, size)

    def __init__(self, width=0, height=0):
        """ Initialize a new instance """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Returns the string representation """

        string = ""
        if self.__height == 0 or self.__width == 0:
            return ''

        for x in range(self.__height):
            for y in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'

        return string[:-1]

    def __repr__(self):
        """ Return the string representation
            to be able to create a new instance
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Calls when an instance is being deleted """

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

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
