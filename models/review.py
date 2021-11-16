#!/usr/bin/python3
"""This module contains the Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """the Review class

    class attributes:
        place_id: string of place id
        user_id: string of user's id
        text: string of user's review
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """initialize Review class"""
        super().__init__(*args, **kwargs)
