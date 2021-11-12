#!/usr/bin/python3
from models.base_model import Basemodel
"""User Module"""


class User(Basemodel):
    """User Public instance"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
