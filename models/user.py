#!/usr/bin/python3
"""The user module that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """the User class

    class attributes:
        email: string of user's email
        password: string of user's password
        first_name: string of user's first name
        last_name: string of user's last name
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """initialize user class"""
        super().__init__(*args, **kwargs)
