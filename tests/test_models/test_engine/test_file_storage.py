#!/usr/bin/python3
"""
This is the unittest for the FileStorage class attributes
and methods.
"""

import unittest
from models.engine.filestorage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    The testfilestrorage class impelements tests for the
    FileStorage class' methods and attributes.
    """

    def setUp(self):
        """
        The setup methods runs first before any other method
        or test in the module, so it is great for creating an instance
        to be tested on multiple methods or anything your would want to
        do repeatedly, which you only have to do once in the method.
        """

        store = FileStorage()

    def test_filestorage(self):
        """ test for the file storage class. """

        self.assertIsNotNone(self.store.__objects)
        self.assertIsNotNone(self.store.__file_path)
        self.assertEqual(self.store.__objects, {})
        self.assertIsInstance(self.store.__objects, dict)
        self.assertIsInstance(self.store.__file_path, str)

    def test_all(self):
        """ The test for the all method """

        file_content = store.all()
        self.assertEqual(self.store.__objects, {})
        self.assertIsNotNone(self.store.__objects)
        self.assertIsInstance(self.store.__objects, dict))

    def test_new(self):
        """ The test for the new method in file storage """
        from model.basemodel import BaseModel

        obj = BaseModel()
        store.new(obj)

        self.assertIsNotNone(self.store.__objects)
        self.assertIsInstance(self.store.__objects, dict)
        self.assertNotEqual(len(self.store.__objects), 0)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIsInstance(self.store.__object[key], BaseModel)

    def test_save(self):
        """ The test for the save method """
        self.assertIsNone(self.store.save())

    def test_reload(self):
        """ Test for the storage reload method """

        self.assertIsNone(self.store.reload())
        store.reload()
        new_dict = store.all()

        self.assertIsNotNone(new_dict)
        self.assertisInstance(new_dict, dict)
