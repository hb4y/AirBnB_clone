#!/usr/bin/python3
'''
    Package initializer
'''

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel', 'Amenity': 'Amenity', 'State': 'State',
           'Place': 'Place', 'Review': 'Review', 'User': 'User'}

storage = FileStorage()
storage.reload()
from models.user import User
"""from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review"""
