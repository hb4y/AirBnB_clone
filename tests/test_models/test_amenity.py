#!/usr/bin/python3
""" test_amenity test files """
# imports
from io import StringIO
import sys
import os
import datetime
import unittest
import models
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        test
    """
    def setUp(self):
        """
            Initializing instance.
        """
        self.amenity = Amenity()

    def TearDown(self):
        """
            Removing the instance.
        """
        del self.amenity

    def test_docstring(self):
        """the test that confirms if everyone has docstring"""
        msg = "Mod does not docstring"
        self.assertIsNotNone(models.amenity.__doc__, msg)
        self.assertIsNotNone(Amenity.__doc__, "Class does not docstring")

    def test_executable_file(self):
        """test if file has permissions to execute"""
        # Check if read access
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check if write access
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check if for execution access
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """check if base_model is an instance of Amenity"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_id(self):
        """test if the id of two instances are different"""
        base_model_ = Amenity()
        base_model_1 = Amenity()
        self.assertNotEqual(base_model_.id, base_model_1.id)

    def test_save(self):
        """check if the attribute updated_at (date) is updated for
        the same object with the current date"""
        base_model_2 = Amenity()
        first_updated = base_model_2.updated_at
        base_model_2.save()
        second_updated = base_model_2.updated_at
        self.assertNotEqual(first_updated, second_updated)
