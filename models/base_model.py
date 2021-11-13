#!/usr/bin/python3
"""
This model is about the BaseModel class that will be inherited by all other classes
"""
from uuid import uuid4
import os
from datetime import datetime
import models


class BaseModel:
    """
    This is class BaseModel whose attributes/methods 
    will be inherited by other classes
    """
    id = ''
    created_at = ''
    updated_at = ''

    def __init__(self, *args, **kwargs):
        """instantiation of BaseModel class
        args: not used
        kwargs: attributes as 'id','created_at','updated_at'
        """
        if id not in kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """returns string representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """returns dictionary of BaseModel"""
        dikt = dict(self.__dict__)
        dikt['__class__'] = self.__class__.__name__
        dikt['created_at'] = self.created_at.isoformat()
        dikt['updated_at'] = self.updated_at.isoformat()
        return dikt
