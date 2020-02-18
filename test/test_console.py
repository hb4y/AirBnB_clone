#!/usr/bin/python3
"""Testing file to test console
"""
#Imports
import pep8
import unittest
import json
import console
import test
import os
#Import console
from console import HBNBCommand
#Import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
#...

class TestConsole(unittest.TestCase):
    """Create testcases for the console
    """
    #first
    @classmethod
    def setUpClass(cls):
        """Called before test the class are run? HHNBCommand
        """
        cls.console = HBNBCommand()
