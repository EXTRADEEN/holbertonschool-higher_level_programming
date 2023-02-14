#!/usr/bin/python3
"""
    Module that creates a class: Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a new rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width proprety """

        return self.__width

    @width.setter
    def width(self, value):
        """ set the width property """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ get the height proprety """

        return self.__height

    @height.setter
    def height(self, value):
        """ set the height property """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ get the x proprety """

        return self.__x

    @x.setter
    def x(self, value):
        """ set the x property """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ get the y proprety """

        return self.__y

    @y.setter
    def y(self, value):
        """ set the y property """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns area of the rectangle """

        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle instance with the character '#' """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ Returns the string representation """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Updates the Rectangle.
        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
                **kwargs (dict): New key/value pairs of attributes
        """

        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.width = v
                if i == 2:
                    self.height = v
                if i == 3:
                    self.x = v
                if i == 4:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """

        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
