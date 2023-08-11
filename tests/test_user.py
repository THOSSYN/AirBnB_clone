#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """A class that tests User class"""
    def setUp(self):
        """Sets up instances/attributes to be used for testing"""
        self.inst1 = User()
        self.inst2 = User(first_name="Busola", last_name="Ife")

    def test_if_subclass(self):
        """Test if User class inherits or is BaseModel's subclass"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_is_instance(self):
        """Test if User is an instance of BaseModel"""
        self.assertIsInstance(self.inst1, BaseModel)

    def test_can_inst_from_kwargs(self):
        """Test if User class can istantiate from dictionary/kwargs"""
        self.assertEqual(self.inst2.last_name, "Ife")


if __name__ == '__main__':
    unittest.main()
