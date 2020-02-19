#!/usr/bin/python3
"""
    Define class review.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Define class review from BaseModel.
    """
    place_id: ""
    user_id: ""
    text: ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
