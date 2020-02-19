#!/usr/bin/python3
"""
    Define class review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Define class review from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Init with super() from BaseModel
        """
        super().__init__(**kwargs)
