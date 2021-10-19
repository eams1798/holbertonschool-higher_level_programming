#!/usr/bin/python3
"""In this module we define a class Base"""

import json


class Base:
    """A class to define the proportions of a geometric figure"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an object for the class Base

        Args:
            id: the Id of the figure
            nb_objects: The number of instantiations the Base did
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries

        Args:
            list_dictionaries: A list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects to
        a file

        Args:
            list_objs: A list of `Rectangle` or `Square` instances
        """
        lst = []
        if list_objs:
            for o in list_objs:
                lst.append(o.to_dictionary())
        text = cls.to_json_string(lst)
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as fjs:
            fjs.write(text)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of a JSON string representation

        Args:
            json_string: A JSON string that stores the representation of
                some objects
        """
        if json_string is None or json_string == "[]":
            return []
        obj = json.loads(json_string)
        return obj

    @classmethod
    def create(cls, **dictionary):
        """Creates a new object with the attributes located in the dictionary

        Args:
            dictionary: A dictionary which contains the attributes to set in
            the new object
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        lst = []
        try:
            with open("{}.json".format(cls.__name__), "r") as fjs:
                jslst = cls.from_json_string(fjs.read())
                for d in jslst:
                    lst.append(cls.create(**d))
                return lst
        except FileNotFoundError:
            return lst
