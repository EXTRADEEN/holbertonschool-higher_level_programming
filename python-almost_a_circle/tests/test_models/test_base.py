#!/usr/bin/python3
"""
    Module that tests differents
    behaviors of the Base class
"""
import unittest
import pycodestyle
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        
    def test_init_with_id(self):
        """
            Test with id for Base class
        """

        base = Base(id=5)
        self.assertEqual(base.id, 5)

    def test_init_without_id(self):
        """
            Test wiyhout id for Base class
        """

        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string_with_empty_list(self):
        """
            Test to json string a empty list for Base class
        """    

        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_list(self):
        """
            Test to json string with a list for Base class
        """

        list_dict = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Mary'}]
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json_str, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Mary"}]')

    def test_save_to_file_with_None(self):
        """
            Test the JSON string representation of the list of
            dictionaries when None is provided should be written 
            to that file
        """

        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            json_str = file.read()
        self.assertEqual(json_str, "[]")
        os.remove("Base.json")

    def test_from_json_string_with_None(self):
        """
            Test with a JSON string when None is
            the output should be an empty list
        """

        list_dict = Base.from_json_string(None)
        self.assertEqual(list_dict, [])
