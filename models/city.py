#!/usr/bin/python3
"""
    Define class City.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Define class City from BaseModel.
    """
    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        """
        Init with super() from BaseModel class
        """
        super().__init__(**kwargs)
