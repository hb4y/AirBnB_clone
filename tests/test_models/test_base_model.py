#!/usr/bin/python3
# Authors:
# test/test_base_model.py.py

"""
    All the test for the base_model are implemented here.
"""
from io import StringIO
import sys
import os
import datetime
import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        Testing in the base class model.
    """

    def setUp(self):
        """
            Initializing instance.
        """
        self.base_model = BaseModel()

    def TearDown(self):
        """
            Removing the instance.
        """
        del self.base_model

    def test_docstring(self):
        """the test that confirms if everyone has docstring"""
        msg = "Mod does not docstring"
        self.assertIsNotNone(models.base_model.__doc__, msg)
        self.assertIsNotNone(BaseModel.__doc__, "Class does not docstring")

    def test_executable_file(self):
        """test if file has permissions to execute"""
        # Check if read access
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check if write access
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check if for execution access
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """check if base_model is an instance of BaseModel"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id(self):
        """test if the id of two instances are different"""
        base_model_ = BaseModel()
        base_model_1 = BaseModel()
        self.assertNotEqual(base_model_.id, base_model_1.id)

    def test_save(self):
        """check if the attribute updated_at (date) is updated for
        the same object with the current date"""
        base_model_2 = BaseModel()
        first_updated = base_model_2.updated_at
        base_model_2.save()
        second_updated = base_model_2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """check if to_dict returns a dictionary, if you add a class
        key with the class name of the object and if updated_at and
        created_at become string objects in the ISO format."""
        my_model3 = BaseModel()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)
