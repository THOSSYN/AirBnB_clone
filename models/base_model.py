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

    def __init__(self, *args, **kwargs):
        """
        The init method is the first method called when an
        instance of the basemodel class is created
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Prints a string reprsentation of instance """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates 'updated_at' instance time"""
        self.updated_at = datetime.now().isoformat()
        return self.updated_at

    def to_dict(self):
        """Returns a dictionary of the attributes of BaseModel class"""
        res_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                res_dict[key] = datetime.isoformat(value)
            else:
                res_dict[key] = value
        # res_dict['__class__'] = self.__class__.__name__
        return res_dict
