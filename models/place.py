#!/usr/bin/env python3
"""Creates a class Place that inherits from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Creates class Place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes the attributes of Place"""
        super().__init__()

    def __str__(self):
        """Returns string representation of the attribute of Place"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
