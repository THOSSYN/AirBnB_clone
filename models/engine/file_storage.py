#!/usr/bin/python3
"""
This is a file storage module that serializes instances to
a JSON file and deserializes JSON file to instances.
"""

import json
import os
from datetime import datetime


class FileStorage:
    """ The file storage class will aid serialization and
    deserialization of basemodel objects, using
    JSON to store the id of each basemodel instance. """

    __file_path = "./model.json"

    # __objects is a dictionary storing all basemodel instance ids
    # the key "<__class__.__name__.id>"
    __objects = {}

    def all(self):
        """ Returns the dictionary of basemodel objects """
        return self.__objects

    def new(self, obj):
        """ Set a new object(obj) in the __object dictionary. """
        #new_key = str(obj.__class__.__name__) + '.' + str(obj.id)
        #self.__objects[new_key] = obj.__dict__
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes the __objects to the json file."""
        data = {}
        for new_key, obj in self.__objects.items():
            data[new_key] = obj.to_dict()
        with open(self.__file_path , "w", encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """ deserializes the JSON file to objects, if __file_path exits
        otherwise nothing is done. """
        from ..base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                des_obj = json.load(f)
                for key, value in des_obj.items():
                    inst = BaseModel(**value)
                    des_obj[key] = inst
            self.__objects = des_obj
