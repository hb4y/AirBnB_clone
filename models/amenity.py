#!/usr/bin/python3
"""
    Define class amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Define class amenity from BaseModel.
    """
    name = ""

    def __init__(self, **kwargs):
        """
        Call super() for BaseModel
        """
        super().__init__(**kwargs)
