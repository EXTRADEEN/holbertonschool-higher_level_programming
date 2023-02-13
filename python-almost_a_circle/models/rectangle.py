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
