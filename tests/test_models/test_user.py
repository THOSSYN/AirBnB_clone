#!/usr/bin/python3
"""
This is a unittest module for the basemodel class.
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from uuid import UUID, uuid4
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    The TestBaseModel is the test for attributes and methods
    in the BaseModel class.
    """

    def setUp(self):
        """ The setup method executes before any test runs. """
        self.ob1 = User()
        self.ob2 = User()
        self.ob1.first_name = "First"
        self.ob1.last_name = "Second"
        self.ob1.email = "airbnb2@email.com"
        self.ob1.my_number = 60
        self.ob2.my_number = 40
        self.inst1 = User()
        self.inst2 = User(first_name="Busola", last_name="Ife")
        self.inst1.email = "tosin@mail.com"
        self.inst1.first_name = "Tosin"
        self.inst1.last_name = "Banwo"
        self.dico = self.ob1.to_dict()

    def test_user(self):
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
        self.assertEqual(self.inst1.last_name, "Banwo")
        self.assertEqual(self.inst2.last_name, "Ife")
        self.assertEqual(self.inst2.first_name, "Busola")

    def test_addy_attr(self):
        """Tests for attributes not inherited from BaseModel"""
        self.assertEqual(self.ob1.first_name, "First")
        self.assertEqual(self.ob1.last_name, "Second")
        self.assertEqual(self.ob1.email, "airbnb2@email.com")

    def test_str(self):
        """ test for the magic print """

        self.assertIsNotNone(self.ob1.__str__.__doc__)

    def test_save(self):
        """ tests the save method """

        self.assertIsNotNone(self.ob1.save().__doc__)

    def test_to_dict(self):
        """ tests for the to dict method """

        self.assertIsNotNone(self.ob1.to_dict().__doc__)
        self.assertIsInstance(self.dico, dict)

    def test_init_from_dict(self):
        """Tests for instantiation from dictionary representation"""
        a_dict = {
                'id': str(uuid4()),
                'created_at': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                }
        ob3 = BaseModel(**a_dict)
        self.assertIsInstance(ob3, BaseModel)
        self.assertEqual(ob3.id, a_dict['id'])
        self.assertEqual(ob3.created_at.isoformat(), a_dict['created_at'])


if __name__ == '__main__':
    unittest.main()
