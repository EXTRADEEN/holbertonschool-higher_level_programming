#!/usr/bin/python3
"""
    Module that creates a class: Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a new rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width proprety """

        return self.__width
    
    @width.setter
    def width(self, value):
        """ set the width property """

    @property
    def height(self):
        """ get the height proprety """

        return self.__height
    
    @height.setter
    def height(self, value):
        """ set the height property """

    @property
    def x(self):
        """ get the x proprety """

        return self.__x
    
    @x.setter
    def x(self, value):
        """ set the x property """

    @property
    def y(self):
        """ get the y proprety """

        return self.__y
    
    @y.setter
    def y(self, value):
        """ set the y property """
