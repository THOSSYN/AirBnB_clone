#!/usr/bin/env python3
"""Creates a City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Creates City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        """Returns the string representation"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
