#!/usr/bin/python3
"""
    Module that creates a new class: Base
"""
import json


class Base:
    """ private class attribute __nb_objects that is set to 0 """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionary):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionary:
            return json.dumps(list_dictionary)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(dict_list)
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """

        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
