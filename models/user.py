#!/usr/bin/env python3
"""A User class that inherits from BaseModel"""

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """Creates a User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        super().__init__()

    def __str__(self):
        """return the string representation of User"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
