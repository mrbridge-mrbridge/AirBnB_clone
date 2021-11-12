"""File Storage"""

import json
from models.base_model import Basemodel
from models.City import City
from models.State import State
from models.Place import Place
from models.User import User
from models.Amenity import Amenity
from models.Review import Review


class FileStorage:
    """File Storage Class"""
    __objects = {}
    __file_path = 'file json'

    def all(self):
        """ returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """ save the objects dictionary into file
        make serializable dict objects """
        temp = {}
        for key, value in type(self).__objects.items():
            temp[key] = value.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(temp) + '\n')

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
         (__file_path) exists ; otherwise, do nothing. If the file doesn’t
         exist, no exception should be raised)"""

        inslist = {'BaseModel': Basemodel, 'City': City, 'State': State,
                   'Place': Place, 'User': User, 'Amenity': Amenity,
                   'Review': Review}
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
            for key, value in json_objects.items():
                self.new(inslist[value['__class__']](**value))
        except FileNotFoundError:
            pass
