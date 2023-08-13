#!/usr/bin/python3
"""
This is a unittest module for the basemodel class.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from uuid import UUID, uuid4
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ 
    The TestBaseModel is the test for attributes and methods
    in the BaseModel class.
    """

    def setUp(self):
        """ The setup method executes before any test runs. """
        self.ob1 = Place()
        self.ob2 = Place()
        self.ob1.name = ""
        self.ob1.city_id = ""
        self.ob1.user_id = ""
        self.ob1.number_rooms = 0
        self.ob2.number_bathrooms = 0

    def test_place(self):
        """ This test for the instance of the basemodel class. """

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

    def test_addy_attr(self):
        """Tests for attributes not inherited from BaseModel"""
        self.assertEqual(self.ob1.name, "")
        self.assertEqual(self.ob1.city_id, "")
        self.assertEqual(self.ob1.user_id, "")
        self.assertIsInstance(self.ob1.number_rooms, int)
        self.assertIsInstance(self.ob2.number_bathrooms, int)

    def test_str(self):
        """ test for the magic print """

        self.assertIsNotNone(self.ob1.__str__.__doc__)

    def test_save(self):
        """ tests the save method """

        self.assertIsNotNone(self.ob1.save().__doc__)

    def test_to_dict(self):
        """ tests for the to dict method """

        self.assertIsNotNone(self.ob1.to_dict().__doc__)

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
