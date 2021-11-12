#!/usr/bin/python3
"""
This model is about the BaseModel class that will be inherited by all other classes
"""
import uuid
import stat
import os
from datetime import datetime

class BaseModel:
    """
    This is class BaseModel whose attributes/methods 
    will be inherited by other classes
    """

    def __init__(self, id, created_at, updated_at):
        """instantiation of class method"""
	self.id = str(uuid.uuid4())
	self.created_at = datetime.fromtimestamp(self.__class__.stat().st_ctime)
	self.updated_at = datetime.fromtimestamp(self.__class__.stat().st_mtime)

    def __str__(self):
	"""prints string representation of class"""
	print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
	"""
    	updates the public instance attribute updated_at 
	with the current datetime
	"""
	self.updated_at = datetime.fromtimestamp(self.__class__.__name__.stat().st_mtime)

    def to_dict(self):
	"""returns dictionary"""
	dikt = self.__dict__
	dikt['__class__'] = self.__class__.__name__
	dikt['created_at'] = self.created_at.isoformat()
	dikt['updated_at'] = self.updated_at.isoformat()
        return dikt
