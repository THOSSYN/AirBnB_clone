#!/usr/bin/env python3
"""Creates a State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Creates class State that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes of class State"""
        super().__init__(**kwargs)

    def __str__(self):
        """Returns a string representation of the attributes of State"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
