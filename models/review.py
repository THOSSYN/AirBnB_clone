#!/usr/bin/env python3
"""Creates a Review class and inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Creates Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *arg, **kwargs):
        """Initializes attributes of class Review"""
        super().__init__(**kwargs)

    def __str__(self):
        """returns string representation of attribute and methods of Review"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
