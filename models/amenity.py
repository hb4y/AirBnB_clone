#!/usr/bin/python3
"""
    Define class amenity
"""
from models.base_model import BaseModel


class amenity(BaseModel):
    """
    Define class amenity from BaseModel.
    """
    name = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
