#!/usr/bin/python3
"""
    Module thet creates a class: Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a new class Square """

    def __init__(self, size, x=0, y=0, id=None):

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Square
        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """

        if args:
            for i, v in enumerate(args):
                if i == 1:
                    self.id = v
                if i == 2:
                    self.size = v
                if i == 3:
                    self.x = v
                if i == 4:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
