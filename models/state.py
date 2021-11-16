#!/usr/bin/python3
"""This module contains the State class which inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """the Sate class

    class attribute:
        
        name: string format of state name
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """initialize State class"""
        super().__init__(*args, **kwargs)
