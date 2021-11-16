#!/usr/bin/python3
"""This module contains the City class which inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """the City class

    class attribute:
        state_id: string format of state.id
        name: string format of city name
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """initialize city class"""
        super().__init__(*args, **kwargs)
