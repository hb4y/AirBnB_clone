#!/usr/bin/python3
# Authors:

"""
    All the test for the base_model are implemented here.
"""
from io import StringIO
import sys
import os
import datetime
import unittest
import models
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
        Testing in the FileStorage class model.
    """

    def setUp(self):
        """
            Initializing instance.
        """
        self.file_storage = FileStorage()

    def TearDown(self):
        """
            Removing the instance.
        """
        del self.file_storage

    def test_docstring(self):
        """the test that confirms if everyone has docstring"""
        msg = "Mod does not docstring"
        self.assertIsNotNone(models.engine.file_storage.__doc__, msg)
        self.assertIsNotNone(FileStorage.__doc__, "Class does not docstring")

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
        self.assertIsInstance(self.file_storage, FileStorage)
