#!/usr/bin/python3
"""This module serializes and deserialize between JSON and instances in a storage engine"""
import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    """This is the FileStorage class

        __objects: dictionary for bjects to be stored
        __file_path: path to the json file
    """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in dict with <obj class name>.id"""
        nu = obj.__class__.__name__
        self.__objects["{}.{}".format(nu, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file"""
        dikt = {}
        for k, v in self.__objects.items():
            dikt[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dikt, f)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objt = json.load(f)
            for k, v in objt.items():
                self.new(eval[v["__class__"]](**v))
        except FileNotFoundError:
            pass
