#!/usr/bin/python3
""" test_amenity test files """
#imports
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase)
""" test """
def test_Amenity_inheritence(self):
        """
             this is proof that if the kind of amenity inherited from the BaseModel
        """
        self.assertIsInstance(Amenity(), BaseModel)

    def test_Amenity_attributes(self):
        """
            this is proof that the "Amenity" class had a name attribute.
        """
        self.assertTrue("name" in Amenity().__dir__())

    def test_Amenity_attribute_type(self):
        """
            this is proof that the Amenity class had the kind of name attribute.
        """
        name_value = getattr(Amenity(), "name")
        self.assertIsInstance(name_value, str)