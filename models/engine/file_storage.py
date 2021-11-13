#!/usr/bin/python3
"""This module serializes and deserialize between JSON and instances in a storage engine"""
import json
import pathlib


class FileStorage:
    """This is the FileStorage class"""

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
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes __objects from JSON file"""
        if __file_path:
            with open(self.__file_path, 'r') as f:
                json.load(f, self.__objects)
