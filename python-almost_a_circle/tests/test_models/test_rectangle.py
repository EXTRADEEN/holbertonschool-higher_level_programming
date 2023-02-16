#!/usr/bin/python3
"""
    Module that tests differents
    behaviors of the Base class
"""
import io
from io import StringIO
from contextlib import redirect_stdout
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        A class to test the Rectangle class
    """

    def test_pep8_base(self):
        """
            Tests that we conform to PEP8
        """

        pep8style = pycodestyle.StyleGuide(quit=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_rectangle_subclass(self):
        """
            Tests if Recangle class inherits
            from Base class
        """

        self.assertTrue(issubclass(Rectangle, Base))
        assert issubclass(Rectangle, Base)

    def test_parameters(self):
        """
            Tests parameters for Rectangle class
        """

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_str(self):
        """
            Tests string parameters for
            a Rectangle class
        """
        r = Rectangle(2, 5, 14, 12, 8)
        self.assertEqual(str(r), "[Rectangle] (8) 14/12 - 2/5")

    def test_type_param(self):
        """
            Tests different types of parameters
            for a Rectangle class
        """

        with self.assertRaises(TypeError):
            Rectangle(2.09, 2)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-5655, 23)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 6)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(3, 5.74)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(True, 2)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(7, 1.78)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(3, "France")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(3, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -865768732657)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(3, 1, 2.797)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(3, 6, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(8, 3, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 3, -86767539)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(3, 2, 16, 4.763)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 2, 76, "other")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 2, False, 9)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-7654767, 4, 7, 6)
            raise ValueError()

    def test_area(self):
        """
            Tests area of a Rectangle class
        """

        r = Rectangle(21, 14)
        self.assertEqual(r.area(), 294)

    def test_display(self):
        """
            Tests for display a Rectangle class
        """

        r = Rectangle(3, 2)
        expected_output = '###\n###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            result = buffer.getvalue()

        r = Rectangle(3, 4, 2, 1)
        expected_output = '\n  ###\n  ###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            result = buffer.getvalue()

        def test_update(self):
            """
                Tests update case
            """

            r = Rectangle(10, 20, 30, 40, 50)
            r.update(1, 3, 5, 6, 4)
            self.assertEqual(r.id, 1)
            self.assertEqual(r.width, 3)
            self.assertEqual(r.height, 5)
            self.assertEqual(r.x, 6)
            self.assertEqual(r.y, 4)

            r.update(id=1, width=3, height=5, x=6, y=4)
            self.assertEqual(r.id, 1)
            self.assertEqual(r.width, 3)
            self.assertEqual(r.height, 5)
            self.assertEqual(r.x, 6)
            self.assertEqual(r.y, 4)

        def to_dictionary(self):
            """
                Tests to dictionary case
            """

            r = Rectangle(3, 8, 1, 6, 12)
            d = r.to_dictionary()
            self.assertIsInstance(d, dict)

        