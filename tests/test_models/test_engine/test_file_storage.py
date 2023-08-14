#!/usr/bin/python3
"""
This is the unittest for the FileStorage class attributes
and methods.
"""

import unittest
from models.engine.file_storage import FileStorage

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

        self.store = FileStorage()

    def test_filestorage(self):
        """ test for the file storage class. """

        with self.assertRaises(AttributeError):
            self.store.__objects
        with self.assertRaises(AttributeError):
            self.store.__file_path

    def test_all(self):
        """ The test for the all method """

        file_content = self.store.all()
        self.assertEqual(file_content, {})
        self.assertIsNotNone(file_content)
        self.assertIsInstance(file_content, dict)

    def test_new(self):
        """ The test for the new method in file storage """
        from models.base_model import BaseModel

        obj = BaseModel()
        ret = self.store.new(obj)
        file_content = self.store.all()

        self.assertIsNone(ret)
        self.assertIsInstance(file_content, dict)
        self.assertNotEqual(len(file_content), 0)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIsInstance(file_content[key], BaseModel)

    def test_save(self):
        """ The test for the save method """
        self.assertIsNone(self.store.save())

    def test_reload(self):
        """ Test for the storage reload method """

        self.assertIsNone(self.store.reload())
        self.store.reload()
        new_dict = self.store.all()

        self.assertIsNotNone(new_dict)
        self.assertIsInstance(new_dict, dict)
