#!/usr/bin/python3
from models.base_model import BaseModel
"""User Module"""

class User(BaseModel):
    """User Public instance"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''


