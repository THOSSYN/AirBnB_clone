#!/usr/bin/env python3
"""Creates an Amenity class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Creates a class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity attribute"""
        super().__init__()

    def __str__(self):
        """Returns string representation of class Amenity"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
