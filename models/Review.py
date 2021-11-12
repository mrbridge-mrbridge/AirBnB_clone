#!/usr/bin/python3
from models.base_model import BaseModel
"""Review Module"""


class Review(BaseModel):
    """Review Public instance"""
    place_id = ''
    user_id = ''
    text = ''
