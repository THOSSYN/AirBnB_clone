#!/usr/bin/env python3
"""A User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Creates a User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__()

    def __str__(self):
        """return the string representation of User"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
