#!/usr/bin/python3
'''
    Package initializer
'''


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

classes = {'BaseModel': 'BaseModel', 'Amenity': 'Amenity', 'State': 'State',
           'Place': 'Place', 'Review': 'Review', 'User': 'User'}

storage = FileStorage()
storage.reload()
