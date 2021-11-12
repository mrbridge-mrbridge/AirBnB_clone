#!/usr/bin/python3
"""The Base_model module"""
import models
from datetime import datetime
import uuid


class Basemodel:
    "The Base_model class"
    currentdatetime = datetime.now()

    def __init__(self, *args, **kwargs):
        """The class constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key = '__class__':
                    continue
                if key in ['created at', 'updated at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__setattr__(key, value)
                    else:
                        self.id = str(uuid.uuid4())
                        self.created_at = datetime
                        self.updated_at = datetime
                        models.storage.new(self)

    def __str__(self):
        """String Format"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        """converts object to dict"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct

    def save(self):
        """saves pbc instance"""
        self.updated_at = datetime.now()
        models.storage.save()
