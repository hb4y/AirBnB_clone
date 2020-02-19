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

    def __init__(self, **kwargs):
        """
        Init with super() from BaseModel
        """
        super().__init__(**kwargs)
