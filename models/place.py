#!/usr/bin/python3
"""This module contains the Place class that inherits from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """the Place class

    class attributes:
        city_id: City.id in string
        user_id: User.id in string
        name: name of place in string
        description: description of place in string
        number_rooms: number of rooms at place in int
        number_bathrooms: number of bathrooms at place in int
        max_guest: Maximum number of guests in int
        price_by_night: Price at night in int
        latitude: in float format
        longitude: in float format
        amenity_ids: Amenity.id in string
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''


    def __init__(self, *args, **kwargs):
        """initialize Place class"""
        super().__init__(*args, **kwargs)
