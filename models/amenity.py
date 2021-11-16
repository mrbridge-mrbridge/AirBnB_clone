#!/usr/bin/python3
"""This module contains the Amenity class which inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """the Amenity class

    class attribute:
        
        name: string format of Amenity name
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """initialize Amenity class"""
        super().__init__(*args, **kwargs)
