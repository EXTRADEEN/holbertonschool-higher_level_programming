#!/usr/bin/python3
""" Module to create inherited class """


class MyList(list):
    """ Creates a new class, MyList thet inherits from list """

    def print_sorted(self):
        """ prints the list, sorted in ascendig sort """
        print(sorted(self))
