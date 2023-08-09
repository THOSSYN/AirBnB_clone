#!/usr/bin/python3
"""
This is a unittest module for the basemodel class.
"""

import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    The TestBaseModel is the test for attributes and methods
    in the BaseModel class.
    """

    def setUp(self):
        """ The setup method executes before any test runs. """
        self.ob1 = BaseModel()
        self.ob2 = BaseModel()
        self.ob1.name = "First"
        self.ob2.name = "Second"
        self.ob1.my_number = 60
        self.ob2.my_number = 40

    def test_basemodel(self):
        """ This test for the instance of the basemodel class. """

        self.assertEqual(self.ob1.my_number, 60)
        self.assertEqual(self.ob2.my_number, 40)
        self.assertNotEqual(self.ob1.id, None)
        self.assertNotEqual(self.ob1.created_at, None)
        self.assertNotEqual(self.ob1.updated_at, None)
        self.assertNotEqual(self.ob1.id, self.ob2.id)
        self.assertIsInstance(UUID(self.ob2.id), UUID)
        self.assertIsInstance(self.ob1.id, str)
        self.assertGreater(self.ob2.created_at, self.ob1.created_at)
        self.assertGreater(self.ob2.created_at, self.ob1.updated_at)
        self.assertIsInstance(self.ob1.created_at, datetime)
        self.assertIsInstance(self.ob1.updated_at, datetime)

    def test_str(self):
        """ test for the magic print """

        self.assertIsNotNone(self.ob1.__str__.__doc__)

    def test_save(self):
        """ tests the save method """

        self.assertIsNotNone(self.ob1.save().__doc__)

    def test_to_dict(self):
        """ tests for the to dict method """

        self.assertIsNotNone(self.ob1.to_dict().__doc__)
