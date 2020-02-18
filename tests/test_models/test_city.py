#!/usr/bin/python3

"""
    All the test for the user model are implemented here.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """
        Testing User class
    """

    def test_City_inheritance(self):
        """
            tests that the City class Inherits from BaseModel
        """