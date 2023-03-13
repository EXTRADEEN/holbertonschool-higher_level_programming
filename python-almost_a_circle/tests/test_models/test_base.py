#!/usr/bin/python3
"""
    Module that tests differents
    behaviors of the Base class
"""
import unittest
import pycodestyle
from models.base import Base


class TestBase(unittest.TestCase):
    """
        A class to test Base class
    """

    def test_pep8_base(self):
        """
            Tests that we conform to PEP8
        """

        pep8style = pycodestyle.StyleGuide(quit=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_init(self):
        """
        Tests attribute id
        """
        b = Base()
        self.assertEqual(b.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b2 = Base(30)
        self.assertEqual(b2.id, 30)
