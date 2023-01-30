#!/usr/bin/python3
""" square """


class Square:
    """ square """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("passsize must be >= 0")
