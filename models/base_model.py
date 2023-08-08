#!/usr/bin/python3
"""
This module contains base class for all of the objects

"""

from datetime import datetime
from uuid import uuid4
class BaseModel:
    """
    The BaseModel class defines the common attributes for
    all other classes inheriting from the base model
    """

    def __init__(self):
        """
        The init method is the first method called when an
        instance of the basemodel class is created
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints a string reprsentation of instance """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
