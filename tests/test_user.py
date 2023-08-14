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
        self.inst1.email = "tosin@mail.com"
        self.inst1.first_name = "Tosin"
        self.inst1.last_name = "Banwo"

    def test_user(self):
        """ Test for the user class set up """
        self.assertIsNotNone(self.inst1.email)
        self.assertIsNotNone(self.inst1.password)
        self.assertIsNotNone(self.inst1.last_name)
        self.assertIsNotNone(self.inst1.first_name)
        self.assertIsInstance(self.inst1.email, str)
        self.assertIsInstance(self.inst1.first_name, str)
        self.assertIsInstance(self.inst1.last_name, str)
        self.assertIsInstance(self.inst1.password, str)
        self.assertEqual(self.inst1.password, "")
        self.assertEqual(self.inst1.email, "tosin@mail.com")
        self.assertEqual(self.inst1.first_name, "Tosin")
        self.assertEqual(self.inst1.first_name, "Banwo")
        self.assertEqual(self.inst2.last_name, "Ife")
        self.assertEqual(self.inst2.first_name, "Busola")

    def test_if_subclass(self):
        """Test if User class inherits or is BaseModel's subclass"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_is_instance(self):
        """Test if User is an instance of BaseModel"""
        self.assertIsInstance(self.inst1, BaseModel)

    def test_can_inst_from_kwargs(self):
        """Test if User class can istantiate from dictionary/kwargs"""
        self.assertEqual(self.inst2.last_name, "Ife")
        self.assertEqual(self.inst2.first_name, "Busola")


if __name__ == '__main__':
    unittest.main()
