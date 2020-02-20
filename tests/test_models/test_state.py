#!/usr/bin/python3
# Authors:
# test/test_state.py.

"""
    All the test for the state are implemented here.
"""
from io import StringIO
import sys
import os
import datetime
import unittest
import models
from models.state import State


class TestReview(unittest.TestCase):
    """
        Testing in the state class.
    """

    def setUp(self):
        """
            Initializing instance.
        """
        self.state = State()

    def TearDown(self):
        """
            Removing the instance.
        """
        del self.state

    def test_docstring(self):
        """the test that confirms if everyone has docstring"""
        msg = "Mod does not docstring"
        self.assertIsNotNone(models.state.__doc__, msg)
        self.assertIsNotNone(State.__doc__, "Class does not docstring")

    def test_executable_file(self):
        """test if file has permissions to execute"""
        # Check if read access
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check if write access
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check if for execution access
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """check if base_model is an instance of BaseModel"""
        self.assertIsInstance(self.state, State)

    def test_id(self):
        """test if the id of two instances are different"""
        base_model_ = State()
        base_model_1 = State()
        self.assertNotEqual(base_model_.id, base_model_1.id)

    def test_save(self):
        """check if the attribute updated_at (date) is updated for
        the same object with the current date"""
        base_model_2 = State()
        first_updated = base_model_2.updated_at
        base_model_2.save()
        second_updated = base_model_2.updated_at
        self.assertNotEqual(first_updated, second_updated)
