#!/usr/bin/python3
"""
    Implementation of the User class from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    '''
        Definition User class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
